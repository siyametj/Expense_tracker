import json

MAIN_EXPENSE_JSON = "main_expense.json"

def total_amount():
    while True:
        try:
            with open(MAIN_EXPENSE_JSON, "r") as file:
                expense = json.load(file)
        except(json.JSONDecodeError, FileNotFoundError):
            print("\nFile not found or file corrupted")
            expense = []
        
        
        total_expense = 0
        if not expense:
            print("Your expense is empty")
            print(f"Total expense : {total_expense}$")
        
        else:
            for item in expense:
                if 'amount' in item and isinstance(item['amount'], (int, float)):
                    total_expense += item['amount'] # type: ignore
            print(f"Total expense : ${total_expense}")


        user_choice = input("Do you want to run again? (yes/no): ")
        if user_choice in ('yes', 'y', 'run again'):
            print("\nSystem run again successfully")
            continue

        elif user_choice in ('no', 'n', 'not'):
            print("\nSystem exit successfully")
            break 
        else:
            print("\nInvalid choice!try yes or no")
            continue

if __name__ == "__main__":
    total_amount()