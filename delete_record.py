import sqlite3

# Connect to the database
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Product ID to delete
product_id = int(input("Enter the Product ID to delete: "))

# Delete the product
cursor.execute('DELETE FROM Products WHERE id = ?', (product_id,))

conn.commit()
conn.close()
print("Product deleted successfully.")
