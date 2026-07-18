import json

MAIN_EXPENSE_JSON = "main_expense.json"

def count_expenses():
    print("-----Count Expenses Function-----")
    try:
        with open(MAIN_EXPENSE_JSON, "r") as file:
            expense = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        expense = []

    if expense:
        length_of_expense = len(expense)
        print(f"Total recorded expenses: {length_of_expense}\n")
    else:
        print("Your expense log is empty.")
        print("Go to the main menu and add some expenses first!\n")

if __name__ == "__main__":
    count_expenses()
