import json

MAIN_EXPENSE_JSON = "main_expense.json"

def search_expense():
    print("-----Search Expenses Function-----")

    while True:
        try:
            with open(MAIN_EXPENSE_JSON, "r") as file:
                expenses = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            print("Expense file is empty or missing.")
            break

        if not expenses:
            print("No expenses to search through.\n")
            break

        try:
            query = input("Search by category, date (YYYY-MM-DD), or description: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            break

        if not query:
            print("Search query cannot be empty.")
            continue

        # Filter the dataset matching any string field
        results = []
        for item in expenses:
            category = str(item.get("category", "")).lower()
            date = str(item.get("date", "")).lower()
            description = str(item.get("description", "")).lower()

            if query in category or query in date or query in description:
                results.append(item)

        # Output results
        if results:
            print(f"\nFound {len(results)} matching expense(s):")
            print(f"{'ID':<6} | {'Amount':<10} | {'Category':<12} | {'Date':<12} | {'Description'}")
            print("-" * 70)
            for item in results:
                print(f"{item.get('id'):<6} | ${item.get('amount', 0.0):<9.2f} | {item.get('category'):<12} | {item.get('date'):<12} | {item.get('description')}")
            print("-" * 70 + "\n")
        else:
            print(f"No records found matching your query: '{query}'\n")

        try:
            another = input("Do you want to search again? (y/n): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            break

        if another in ('y', 'yes'):
            continue
        else:
            print("Exiting search utility...\n")
            break

if __name__ == "__main__":
    search_expense()
