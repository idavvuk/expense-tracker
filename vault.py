import csv

expenses_file_path = 'expenses.csv'




def add_expense(): 
    date = input("add date ")
    amount = input("add amount ")
    category = input("add category ")


    with open(expenses_file_path, 'w', newline = '') as csvfile:
        w = csv.writer(csvfile)
        w.writerow([date, amount, category])
        print("Expense successfully added!")

def view_expenses():
    
    with open("expenses_file_path", "r") as file: 
        reader = csv.reader(file)
        next(reader) #what does reader do? 
        for row in reader: 
            print(row)









