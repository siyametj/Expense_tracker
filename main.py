import sys

# Correctly import the modules matching your actual file names
import add_expense
import view_expense
import search_expense
import delete_specific_expense
import edit_expense
import count_expenses
import clear_all_expenses
import export_to_txt

def main_menu():
    while True:
        print("====== EXPENSE TRACKER DASHBOARD ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search Expense")
        print("4. Delete Specific Expense")
        print("5. Edit Expense")
        print("6. Count Total Expenses")
        print("7. Clear All Expenses")
        print("8. Export Expenses to TXT File")
        print("9. Exit Application")
        print("=======================================")

        try:
            choice = input("Select an option (1-9): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nShutting down application. Goodbye!")
            sys.exit(0)

        if not choice:
            print("Input cannot be empty. Please enter a number between 1 and 9.\n")
            continue

        if choice == '1':
            add_expense.add_expense()
        elif choice == '2':
            view_expense.view_expense()
        elif choice == '3':
            search_expense.search_expense()
        elif choice == '4':
            delete_specific_expense.delete_expense()
        elif choice == '5':
            edit_expense.edit_expense()
        elif choice == '6':
            count_expenses.count_expenses()
        elif choice == '7':
            clear_all_expenses.clear_all_expense()
        elif choice == '8':
            export_to_txt.export_to_txt()
        elif choice == '9':
            print("Exiting application safely. Goodbye!")
            break
        else:
            print(f"'{choice}' is an invalid selection! Please enter a number from 1 to 9.\n")

if __name__ == "__main__":
    main_menu()
