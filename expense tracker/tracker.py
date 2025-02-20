
def load_expenses():
    try:
        with open('expenses.txt','r') as file:
            return [eval(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        return []
    
def save_expenses(expenses):
    with open('expenses.txt', 'w') as file:
        for expense in expenses:
            file.write(str(expense) + '\n')

def add_expense(expenses):
    try:
        amount = float(input('Enter amount to spend: '))
        category = input("Enter category (food, transport, bills, etc):")
        description = input('Enter description: ')

        expense = {
            'amount': amount,
            'category': category,
            'description': description
        }

        expenses.append(expense)
        save_expenses(expenses)
        print('Expense added succesfully!')
    except ValueError:
            print('Please enter a valid amount!')

def view_expenses(expenses):
    if not expenses:
          print("No expenses recorded yet!")     
          return
    
    print('\nYour Expenses: ') 
    print('-' * 50)
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. Amount: ${expense['amount']:.2f} |"
               f"Category: {expense['category']} |"
               f"Description: {expense['description']}")
    print('-' * 50)
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Spent: ${total:.2f}")
      

expenses = load_expenses()
while True:
    choice = input("""\nExpense Tracker Menu:
1.Add Expense
2.view Expenses
3.Quit
Your choice: """)
    
    if choice == '1':
        add_expense(expenses)
    elif choice == '2':
        view_expenses(expenses)
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")