import vault

def start(): 
    choice = input("Add expense [A], View expenses [V]: ").lower() 
    if choice == "a":
        vault.add_expense()
    if choice == "v":
        vault.view_expenses()