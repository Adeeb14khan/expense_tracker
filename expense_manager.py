from db import add_expense, fetch_expenses, delete_expense

def input_expense(conn):
    date = input("Date (YYYY-MM-DD): ").strip()
    category = input("Category: ").strip()
    amount = float(input("Amount: ").strip())
    description = input("Description: ").strip()
    add_expense(conn, date, category, amount, description)
    print("Expense added successfully.")

def list_expenses(conn, filter_category=None):
    expenses = fetch_expenses(conn, filter_category)
    print("\n--- Expenses ---")
    print("ID | Date | Category | Amount | Description")
    for exp in expenses:
        print(f"{exp[0]} | {exp[1]} | {exp[2]} | {exp[3]:.2f} | {exp[4]}")

def remove_expense(conn):
    expense_id = int(input("Enter Expense ID to delete: "))
    delete_expense(conn, expense_id)
    print("Deleted successfully.")
