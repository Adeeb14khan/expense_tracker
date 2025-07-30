from db import create_connection, create_table
from expense_manager import input_expense, list_expenses, remove_expense
from report import expenses_summary, export_to_csv

def show_menu():
    print("\n=== Personal Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Expenses by Category")
    print("4. Delete Expense")
    print("5. Show Category Summary")
    print("6. Export to CSV")
    print("0. Exit")

def main():
    conn = create_connection()
    create_table(conn)

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            input_expense(conn)
        elif choice == "2":
            list_expenses(conn)
        elif choice == "3":
            category = input("Filter by category: ")
            list_expenses(conn, category)
        elif choice == "4":
            remove_expense(conn)
        elif choice == "5":
            expenses_summary(conn)
        elif choice == "6":
            export_to_csv(conn)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

