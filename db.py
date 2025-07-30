import sqlite3

DB_NAME = "expenses.db"

def create_connection(db_name=DB_NAME):
    return sqlite3.connect(db_name)

def create_table(conn):
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                description TEXT
            )
        ''')

def add_expense(conn, date, category, amount, description):
    with conn:
        conn.execute(
            "INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
            (date, category, amount, description)
        )

def fetch_expenses(conn, filter_category=None):
    cursor = conn.cursor()
    if filter_category:
        cursor.execute("SELECT * FROM expenses WHERE category = ?", (filter_category,))
    else:
        cursor.execute("SELECT * FROM expenses")
    return cursor.fetchall()

def delete_expense(conn, expense_id):
    with conn:
        conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
