import json

MAIN_EXPENSE_JSON = "main_expense.json"

def delete_expense():
    print("-----Delete Specific Expense Function-----")

    while True:
        try:
            with open(MAIN_EXPENSE_JSON, "r") as file:
                expense = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            print("Warning: File not found or corrupted.")
            expense = []

        if not expense:
            print("No expenses present to delete!\n")
            break

        try:
            user_input_id = int(input("Enter the Expense ID you want to delete: "))
        except ValueError:
            print("Expense ID must be an integer. Try again.")
            continue
        except (EOFError, KeyboardInterrupt):
            print("\nExiting delete function...")
            break

        # Find matching item by ID
        target_expense = None
        for info in expense:
            if info['id'] == user_input_id:
                target_expense = info
                break

        if target_expense:
            # Confirm details safely
            print("-" * 50)
            print(f"1. Expense ID          : {target_expense.get('id')}")
            print(f"2. Expense Amount      : {target_expense.get('amount', 0)}$")
            print(f"3. Expense Category    : {target_expense.get('category', 'N/A')}")
            print(f"4. Expense Date        : {target_expense.get('date', 'N/A')}")
            print(f"5. Expense Description : {target_expense.get('description', 'N/A')}")
            print("-" * 50)

            try:
                print("Are you sure you want to delete this expense?")
                user_choice = input("Enter 'y' to confirm or 'n' to cancel: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                break

            if user_choice in ('yes', 'y'):
                expense.remove(target_expense)
                try:
                    with open(MAIN_EXPENSE_JSON, 'w') as file:
                        json.dump(expense, file, indent=4)
                    print("Expense deleted successfully!")
                except IOError as e:
                    print(f"Error saving changes: {e}")
            else:
                print("Delete operation cancelled.")
        else:
            print(f"No expense found matching ID: {user_input_id}")

        # Check loop repetition choice
        try:
            user_choice = input("\nDo you want to delete another expense? (yes/no): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            break

        if user_choice in ('yes', 'y'):
            print("System resetting...\n")
            continue
        else:
            print("Exiting to menu...\n")
            break

if __name__ == "__main__":
    delete_expense()
