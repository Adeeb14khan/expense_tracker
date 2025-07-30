from db import create_connection, create_table, add_expense

def main():
    conn = create_connection()
    create_table(conn)
    print("Add a new expense:")
    date = input("Date (YYYY-MM-DD): ")
    category = input("Category: ")
    amount = float(input("Amount: "))
    description = input("Description: ")
    add_expense(conn, date, category, amount, description)
    print("Expense added successfully.")

if __name__ == "__main__":
    main()
