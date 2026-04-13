import sqlite3

# Connect to the ecommerce.db database
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Retrieve all records from the Products table
cursor.execute("SELECT * FROM Products")
products = cursor.fetchall()

# Display the retrieved records
print("Product List:")
for product in products:
    print(product)

# Close the connection
conn.close()
