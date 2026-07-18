import json

MAIN_EXPENSE_JSON = "main_expense.json"
EXPORT_TXT_FILE = "expense_report.txt"

def export_to_txt():
    print("-----Export to TXT Function-----")

    try:
        with open(MAIN_EXPENSE_JSON, "r") as file:
            expenses = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        print("No expenses found to export or file is missing.")
        return

    if not expenses:
        print("Your expense database is empty. Nothing to export.")
        return

    try:
        # Open the file ONCE in write mode to start fresh, then write everything
        with open(EXPORT_TXT_FILE, "w") as text_file:
            text_file.write("=" * 40 + "\n")
            text_file.write("         EXPENSE REPORT LOG           \n")
            text_file.write("=" * 40 + "\n\n")

            for info in expenses:
                text_file.write(f"ID          : {info.get('id', 'N/A')}\n")
                text_file.write(f"Amount      : {info.get('amount', 0.0)}$\n")
                text_file.write(f"Category    : {info.get('category', 'N/A')}\n")
                text_file.write(f"Date        : {info.get('date', 'N/A')}\n")
                text_file.write(f"Description : {info.get('description', 'N/A')}\n")
                text_file.write("-" * 40 + "\n")

        print(f"Success! All expenses exported cleanly to '{EXPORT_TXT_FILE}'.\n")

    except IOError as e:
        print(f"Failed to write file out to text format: {e}")

if __name__ == "__main__":
    export_to_txt()
