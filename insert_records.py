import sqlite3

# Connect to the ecommerce.db database
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Data to be inserted (example records)
products_to_insert = [
    ("Laptop", 999.99, 10, "Electronics"),
    ("Smartphone", 699.99, 25, "Electronics"),
    ("Coffee Maker", 49.99, 15, "Home Appliances"),
    ("Book", 19.99, 50, "Books"),
    ("T-Shirt", 15.99, 30, "Clothing")
]

# Insert multiple records into the Products table
cursor.executemany('''
    INSERT INTO Products (name, price, quantity, category) 
    VALUES (?, ?, ?, ?)
''', products_to_insert)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Records inserted successfully.")
