import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
DROP TABLE IF EXISTS transactions
""")

cursor.execute("""
CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    type TEXT NOT NULL,
    category_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    amount REAL NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id)
)
""")

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS categories (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL
# )
# """)

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS transactions (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     date TEXT NOT NULL,
#     type TEXT NOT NULL,
#     category TEXT NOT NULL,
#     description TEXT NOT NULL,
#     amount REAL NOT NULL
# )
# """)

conn.commit()
conn.close()