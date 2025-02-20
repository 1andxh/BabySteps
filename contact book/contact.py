class Contact:
    def __init__(self, name, phone, email="",address=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self) -> None:
        self.contacts = []

    def add_contacts(self):
        print('\n=== Add new contact ===')
        name = input("Enter name of contact: ")
        try:
            phone = int(input('Enter phone number: '))
        except ValueError:
            print('Enter numbers only')
        email = input('Enter email address(optional)')
        address = input('Enter address(optional)')

        contact = Contact(name,phone,email,address)
        self.contacts.append(contact)
        print("Contact Added succesfully!")


    def view_contacts(self):
        if not self.contacts:
            print("\nNo contacts found")
            return
        print('\n=== Contact Lists ===')
        for i,contact in enumerate(self.contacts, 1):
            print(f'\nContact {i}:')
            print(f'Name: {contact.name}')
            print(f'Phone: {contact.phone}')
            if contact.email:
                print(f'Email: {contact.email}')
            if contact.address:
                print(f'Address: {contact.address}')

    def search_contacts(self):
        pass