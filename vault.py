import csv




entry = []
all_entries = [[]]

def add_expense(): 
    while True: 
        date = input("add date ")
        amount = input("add amount ")
        category = input("add category ")
        entry.append({date, amount, category })
        if date == "":
            break
        all_entries.append({entry})
    print(all_entries)

def view_expenses():
    print(all_entries)



