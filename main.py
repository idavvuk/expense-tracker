import vault
import sys
import pandas as pd # type: ignore


def main(): 
    while True: 
        print("Welcome to your expense tracker!")
        while True: 
            choice = input("Choose one: [A] Add expense, [V] View expense").lower()
        if choice == "a":
            vault.add_expense()
        elif choice == "v":
            vault.view_expenses
        else: 
            print("Invalid choice")
main()
        
            
        