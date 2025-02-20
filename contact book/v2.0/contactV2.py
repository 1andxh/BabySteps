import customtkinter as ctk
import json
from pathlib import Path
from CTkTable import CTkTable  
from CTkMessagebox import CTkMessagebox  

# Set appearance mode and default color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Contact:
    def __init__(self, name, phone, email="", address=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
    
    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(**data)

class ContactBookGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure main window
        self.title("Modern Contact Book")
        self.geometry("1000x600")
        
        # Initialize contacts list and current selection
        self.contacts = []
        self.current_contact = None
        
        # Load existing contacts
        self.load_contacts()
        
        # Create the GUI elements
        self.create_gui()
        
        # Update the contact list
        self.update_contact_list()
    
    def create_gui(self):
        # Create main frames
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Left frame (Contact List)
        self.left_frame = ctk.CTkFrame(self)
        self.left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        # Right frame (Contact Details)
        self.right_frame = ctk.CTkFrame(self)
        self.right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        self.create_search_bar()
        self.create_contact_list()
        self.create_contact_form()
        self.create_buttons()
    
    def create_search_bar(self):
        # Search frame
        search_frame = ctk.CTkFrame(self.left_frame)
        search_frame.pack(fill="x", padx=10, pady=10)
        
        # Search label
        search_label = ctk.CTkLabel(search_frame, text="Search Contacts:")
        search_label.pack(side="left", padx=5)
        
        # Search entry
        self.search_var = ctk.StringVar()
        self.search_var.trace('w', self.search_contacts)
        self.search_entry = ctk.CTkEntry(search_frame, textvariable=self.search_var,
                                       placeholder_text="Search by name or phone...")
        self.search_entry.pack(side="left", fill="x", expand=True, padx=5)
    
    def create_contact_list(self):
        # Contact list frame with title
        list_frame = ctk.CTkFrame(self.left_frame)
        list_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        
        # Title for the list
        list_label = ctk.CTkLabel(list_frame, text="Contacts", 
                                 font=ctk.CTkFont(size=16, weight="bold"))
        list_label.pack(pady=5)
        
        # Create table for contacts
        self.table = CTkTable(list_frame, values=[["Name", "Phone"]], 
                             header_color="gray30")
        self.table.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Bind selection event
        self.table.bind("<ButtonRelease-1>", self.on_select_contact)
    
    def create_contact_form(self):
        # Form title
        form_label = ctk.CTkLabel(self.right_frame, text="Contact Details",
                                 font=ctk.CTkFont(size=20, weight="bold"))
        form_label.pack(pady=20)
        
        # Create form fields
        fields_frame = ctk.CTkFrame(self.right_frame)
        fields_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Name field
        ctk.CTkLabel(fields_frame, text="Name:").pack(anchor="w", padx=5, pady=(10, 0))
        self.name_var = ctk.StringVar()
        self.name_entry = ctk.CTkEntry(fields_frame, textvariable=self.name_var,
                                     placeholder_text="Enter name...")
        self.name_entry.pack(fill="x", padx=5, pady=(0, 10))
        
        # Phone field
        ctk.CTkLabel(fields_frame, text="Phone:").pack(anchor="w", padx=5, pady=(10, 0))
        self.phone_var = ctk.StringVar()
        self.phone_entry = ctk.CTkEntry(fields_frame, textvariable=self.phone_var,
                                      placeholder_text="Enter phone number...")
        self.phone_entry.pack(fill="x", padx=5, pady=(0, 10))
        
        # Email field
        ctk.CTkLabel(fields_frame, text="Email:").pack(anchor="w", padx=5, pady=(10, 0))
        self.email_var = ctk.StringVar()
        self.email_entry = ctk.CTkEntry(fields_frame, textvariable=self.email_var,
                                      placeholder_text="Enter email...")
        self.email_entry.pack(fill="x", padx=5, pady=(0, 10))
        
        # Address field
        ctk.CTkLabel(fields_frame, text="Address:").pack(anchor="w", padx=5, pady=(10, 0))
        self.address_var = ctk.StringVar()
        self.address_entry = ctk.CTkEntry(fields_frame, textvariable=self.address_var,
                                        placeholder_text="Enter address...")
        self.address_entry.pack(fill="x", padx=5, pady=(0, 10))
    
    def create_buttons(self):
        # Buttons frame
        button_frame = ctk.CTkFrame(self.right_frame)
        button_frame.pack(fill="x", padx=20, pady=20)
        
        # Add button
        self.add_button = ctk.CTkButton(button_frame, text="Add New",
                                      command=self.add_contact)
        self.add_button.pack(side="left", padx=5)
        
        # Save button
        self.save_button = ctk.CTkButton(button_frame, text="Save",
                                       command=self.save_contact)
        self.save_button.pack(side="left", padx=5)
        
        # Delete button
        self.delete_button = ctk.CTkButton(button_frame, text="Delete",
                                         command=self.delete_contact,
                                         fg_color="red", hover_color="darkred")
        self.delete_button.pack(side="left", padx=5)
        
        # Clear button
        self.clear_button = ctk.CTkButton(button_frame, text="Clear",
                                        command=self.clear_form,
                                        fg_color="gray40", hover_color="gray30")
        self.clear_button.pack(side="left", padx=5)
    
    def add_contact(self):
        self.current_contact = None
        self.clear_form()
        self.name_entry.focus()
    
    def save_contact(self):
        name = self.name_var.get().strip()
        phone = self.phone_var.get().strip()
        
        if not name or not phone:
            CTkMessagebox(title="Error", message="Name and phone are required!",
                         icon="cancel")
            return
        
        contact = Contact(
            name=name,
            phone=phone,
            email=self.email_var.get().strip(),
            address=self.address_var.get().strip()
        )
        
        if self.current_contact is not None:
            self.contacts[self.current_contact] = contact
        else:
            self.contacts.append(contact)
        
        self.save_contacts()
        self.update_contact_list()
        self.clear_form()
        CTkMessagebox(title="Success", message="Contact saved successfully!",
                     icon="check")
    
    def delete_contact(self):
        if self.current_contact is None:
            CTkMessagebox(title="Error", message="Please select a contact to delete!",
                         icon="cancel")
            return
        
        msg = CTkMessagebox(title="Confirm Delete",
                           message="Are you sure you want to delete this contact?",
                           icon="question", option_1="No", option_2="Yes")
        
        if msg.get() == "Yes":
            del self.contacts[self.current_contact]
            self.save_contacts()
            self.update_contact_list()
            self.clear_form()
    
    def clear_form(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.email_var.set("")
        self.address_var.set("")
        self.current_contact = None
    
    def on_select_contact(self, event):
        try:
            selection = self.table.get_selected_row()
            if selection is None:
                return
            
            contact_idx = selection - 1  # Subtract 1 to account for header row
            if contact_idx < 0 or contact_idx >= len(self.contacts):
                return
                
            contact = self.contacts[contact_idx]
            self.current_contact = contact_idx
            
            self.name_var.set(contact.name)
            self.phone_var.set(contact.phone)
            self.email_var.set(contact.email)
            self.address_var.set(contact.address)
        except Exception as e:
            print(f"Error selecting contact: {e}")
    
    def search_contacts(self, *args):
        self.update_contact_list()
    
    def update_contact_list(self):
        # Prepare the data for the table
        table_data = [["Name", "Phone"]]  # Header row
        
        # Filter contacts based on search term
        search_term = self.search_var.get().lower()
        for contact in self.contacts:
            if (search_term in contact.name.lower() or 
                search_term in contact.phone.lower()):
                table_data.append([contact.name, contact.phone])
        
        # Update the table
        self.table.update_values(table_data)
    
    def load_contacts(self):
        try:
            with open('contacts.json', 'r') as f:
                contacts_data = json.load(f)
                self.contacts = [Contact.from_dict(data) for data in contacts_data]
        except FileNotFoundError:
            self.contacts = []
    
    def save_contacts(self):
        contacts_data = [contact.to_dict() for contact in self.contacts]
        with open('contacts.json', 'w') as f:
            json.dump(contacts_data, f, indent=2)

def main():
    app = ContactBookGUI()
    app.mainloop()

if __name__ == "__main__":
    main()