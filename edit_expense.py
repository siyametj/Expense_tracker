import json

MAIN_EXPENSE_JSON = "main_expense.json"

def edit_expense():
    print("-----Edit Expense Function-----")

    while True:
        try:
            with open(MAIN_EXPENSE_JSON, "r") as file:
                expense = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            print("\nFile not found or corrupted.")
            return

        try:
            user_expense_id = int(input("Enter expense id to edit: "))
        except ValueError:
            print("Enter a valid integer ID.")
            continue
        except (EOFError, KeyboardInterrupt):
            print("\nExiting edit function...")
            break

        found_exp = None
        for exp in expense:
            if exp['id'] == user_expense_id:
                found_exp = exp
                break

        if not found_exp:
            print(f"No expense found with ID {user_expense_id}")
            continue

        print(f"\nFound Expense ID {user_expense_id}:")
        print(f"Amount: {found_exp['amount']}$")
        print(f"Category: {found_exp['category']}")
        print(f"Date: {found_exp['date']}")
        print(f"Description: {found_exp['description']}")
        print("-" * 50)

        print("\nWhich data field do you want to edit?")
        print("1. Amount")
        print("2. Category")
        print("3. Date")
        print("4. Description")

        try:
            choice = input("Enter choice (1-4 or name): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            break

        # Consolidate selection options mapping logic
        if choice in ('1', 'amount'):
            try:
                new_amount = float(input("Enter new amount: "))
                found_exp["amount"] = new_amount
                print("Amount updated successfully!")
            except ValueError:
                print("Invalid input! Amount must be a number.")
                continue

        elif choice in ('2', 'category'):
            categories = ['food', 'bill', 'shopping', 'travel']
            print(f"Allowed choices: {categories}")
            new_cat = input("Enter new category: ").strip().lower()
            if new_cat in categories:
                found_exp["category"] = new_cat
                print("Category updated successfully!")
            else:
                print("Invalid category matching failed. Field not updated.")
                continue

        elif choice in ('3', 'date'):
            new_date = input("Enter new date (YYYY-MM-DD): ").strip()
            if new_date:
                found_exp["date"] = new_date
                print("Date updated successfully!")
            else:
                print("Date cannot be empty.")
                continue

        elif choice in ('4', 'description'):
            new_desc = input("Enter new description: ").strip()
            found_exp["description"] = new_desc if new_desc else "No description provided"
            print("Description updated successfully!")

        else:
            print("Invalid choice selection! Try again.")
            continue

        # Save updates to disk
        try:
            with open(MAIN_EXPENSE_JSON, "w") as file:
                json.dump(expense, file, indent=4)
        except IOError as e:
            print(f"Failed to update file: {e}")

        # Continuation validation section
        try:
            user_choice = input("\nDo you want to edit another expense? (yes/no): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            break

        if user_choice in ("yes", "y"):
            print("Resetting configuration loop...\n")
            continue
        else:
            print("Exiting to menu...\n")
            break

if __name__ == "__main__":
    edit_expense()
