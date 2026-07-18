import json
import datetime

MAIN_EXPENSE_JSON = "main_expense.json"

def add_expense():
    """Add expense to the json file"""
    print("-----Add Expense Function-----")

    while True:
        # 1. Load data safely inside the loop loop context
        try:
            with open(MAIN_EXPENSE_JSON, "r") as file:
                expenses = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            expenses = []

        # 2. Amount Input Section
        print("\n1. Enter expense amount.")
        try:
            user_amount = float(input("Enter amount$ : "))
            if user_amount < 0:
                print("Amount cannot be negative. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        except (EOFError, KeyboardInterrupt):
            print("\nExiting program...")
            break

        print("Amount Granted")

        # 3. Category Input Loop (Isolated so it doesn't reset the amount!)
        categories = ['food', 'bill', 'shopping', 'travel']
        print(f"\n2. Please enter category. Options: {categories}")

        while True:
            try:
                user_category = input("Enter category name : ").lower().strip()
            except (EOFError, KeyboardInterrupt):
                user_category = ""
                break

            if user_category in categories:
                print("Category granted")
                break
            else:
                print(f"Invalid category! Choose strictly from: {categories}")

        if not user_category:  # Handles abrupt exits inside the nested loop
            break

        # 4. Date Input Section
        print("\n3. Please enter date")
        try:
            user_date = input("Enter the date (YYYY-MM-DD) or press Enter for today: ").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if user_date:
            # Simple fallback validation format check
            try:
                datetime.datetime.strptime(user_date, "%Y-%m-%d")
                print("Date granted")
            except ValueError:
                print("Invalid format! Defaulting to today's date instead.")
                user_date = datetime.datetime.now().strftime("%Y-%m-%d")
        else:
            today = datetime.datetime.now()
            user_date = today.strftime("%Y-%m-%d")
            print("Default today date added\n")

        # 5. Description Input Section
        print("4. Enter description of expense")
        try:
            user_description = input("Enter description : ").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if not user_description:
            user_description = "No description provided"
            print("No description entered. Default used.")
        else:
            print("Description granted\n")

        # 6. Safe ID Generation (Prevents duplicate IDs upon deletions)
        expense_id = max([e["id"] for e in expenses], default=0) + 1

        # 7. Package and Append Data
        expense_data = {
            "id": expense_id,
            "amount": user_amount,
            "category": user_category,
            "date": user_date,
            "description": user_description
        }
        expenses.append(expense_data)

        try:
            with open(MAIN_EXPENSE_JSON, "w") as file:
                json.dump(expenses, file, indent=4)
            print("Expense saved successfully!")
        except Exception as e:
            print(f"Error saving to file: {e}")

        # 8. Loop Continuity Prompt
        try:
            choice = input("\nDo you want to run again (y/n): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            break

        if choice in ('y', 'yes'):
            print("System running again successfully\n")
            continue
        else:
            print("System Exit successfully!")
            break

if __name__ == "__main__":
    add_expense()
