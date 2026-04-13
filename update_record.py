import sqlite3

# Connect to the database
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Product ID to update
product_id = int(input("Enter the Product ID to update: "))

# New details for the product
new_price = float(input("Enter the new price: "))
new_quantity = int(input("Enter the new quantity: "))

# Update the product record
cursor.execute('''
    UPDATE Products 
    SET price = ?, quantity = ? 
    WHERE id = ?
''', (new_price, new_quantity, product_id))

conn.commit()
conn.close()
print("Product updated successfully.")
