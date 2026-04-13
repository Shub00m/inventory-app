import sqlite3

# Connect to SQLite Database (it will create 'ecommerce.db' if it doesn't exist)
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Create Products Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL,
        category TEXT
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and 'Products' table created successfully.")
