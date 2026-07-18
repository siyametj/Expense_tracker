import json

MAIN_EXPENSE_JSON = "main_expense.json"

def view_expense():
    print("-----View All Expenses Function-----")

    try:
        with open(MAIN_EXPENSE_JSON, "r") as file:
            expenses = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        expenses = []

    if not expenses:
        print("Your expense log is currently empty.\n")
        return

    # Create a clean, readable tabular layout
    print(f"{'ID':<6} | {'Amount':<10} | {'Category':<12} | {'Date':<12} | {'Description'}")
    print("-" * 70)

    for item in expenses:
        eid = item.get("id", "N/A")
        amount = f"${item.get('amount', 0.0):.2f}"
        category = item.get("category", "N/A")
        date = item.get("date", "N/A")
        desc = item.get("description", "No description")

        print(f"{eid:<6} | {amount:<10} | {category:<12} | {date:<12} | {desc}")
    print("-" * 70 + "\n")

if __name__ == "__main__":
    view_expense()
