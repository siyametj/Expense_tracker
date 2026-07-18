# 💰 Modular Expense Tracker

A lightweight, terminal-based **Expense Tracker** built with **Python**. The application follows a clean modular architecture where each feature is separated into its own module and managed through a central dashboard controller. Expense data is stored locally in a JSON database, making the application simple, portable, and dependency-free.

---

## ✨ Features

- ➕ **Add Expenses**
  - Supports decimal values
  - Prevents negative amounts
  - Validates expense categories
  - Automatically formats dates

- 📋 **View Expenses**
  - Display all expenses in a clean, readable table.

- 🔍 **Search Expenses**
  - Search by:
    - Category
    - Date
    - Description

- ✏️ **Edit Expenses**
  - Update existing records, including:
    - Amount
    - Category
    - Date
    - Description

- 🗑️ **Delete Expenses**
  - Remove an expense by its unique ID with confirmation before deletion.

- 📊 **Expense Counter**
  - Instantly view the total number of recorded expenses.

- ⚠️ **Clear All Expenses**
  - Delete all records with built-in confirmation to prevent accidental data loss.

- 📄 **Export Reports**
  - Generate a formatted `.txt` report containing all recorded expenses.

---

## 📂 Project Structure

```text
expense-tracker/
│
├── main.py                      # Main application dashboard
├── add_expense.py               # Add new expenses
├── view_expense.py              # Display all expenses
├── search_expense.py            # Search functionality
├── edit_expense.py              # Edit existing expenses
├── delete_specific_expense.py   # Delete expense by ID
├── count_expenses.py            # Count total expenses
├── clear_all_expenses.py        # Clear all expense records
├── export_to_txt.py             # Export expenses to TXT
│
├── main_expense.json            # Local JSON database (auto-generated)
├── expense_report.txt           # Exported report (auto-generated)
└── .gitignore
```

---

## 🛠️ Installation

### Clone the repository

```bash
git clone https://github.com/siyametj/Expense_tracker
cd expense-tracker
```

### Run the application

This project uses only Python's built-in libraries, so **no external dependencies** are required.

```bash
python main.py
```

---

## 💾 Data Storage

The application automatically creates and manages:

- `main_expense.json` — Stores all expense records.
- `expense_report.txt` — Generated when exporting expense reports.

These generated files are included in `.gitignore` to prevent local data from being committed to the repository.

---

## 📌 Supported Categories

- 🍔 Food
- 💡 Bill
- 🛍️ Shopping
- ✈️ Travel

---

## 🖥️ Technologies Used

- Python 3
- JSON
- Standard Library Only

---

## 🎯 Design Goals

- Modular and maintainable codebase
- Easy to extend with new features
- Lightweight and dependency-free
- Beginner-friendly project structure
- Clean terminal interface

---

## 📜 License

This project is open source and available under the **MIT License**.
