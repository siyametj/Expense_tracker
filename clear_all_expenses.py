import json

MAIN_EXPENSE_JSON = "main_expense.json"

def clear_all_expense():
    print("-----Clear All Expense Function-----")

    while True:
        try:
            print("\nDo you want to remove all expenses?")
            print("1. Yes - remove all expenses")
            print("2. No - cancel operation")
            print("3. Exit - return to menu")
            user_choice = input("\nEnter your choice (1-3 or text): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting system...")
            break

        if not user_choice:
            print("You entered nothing, system stopped.")
            break

        # Process choice values
        if user_choice in ('1', 'yes', 'remove', 'delete', 'del'):
            action = "remove"
        elif user_choice in ('2', 'no', 'not', 'n', 'cancel'):
            action = "cancel"
        elif user_choice in ('3', 'exit', 'quit', 'ext'):
            action = "exit"
        else:
            print("Invalid syntax/choice. Try again.")
            continue

        # Execute actions based on choice
        if action == "remove":
            try:
                # Write an empty list to wipe out the data
                with open(MAIN_EXPENSE_JSON, 'w') as file:
                    json.dump([], file, indent=4)
                print("All expenses removed successfully!\n")
            except IOError as e:
                print(f"Error modifying file: {e}\n")
            break

        elif action == "cancel":
            print("Operation cancelled.\n")
            break

        elif action == 'exit':
            print("Exiting to menu...\n")
            break

if __name__ == "__main__":
    clear_all_expense()
