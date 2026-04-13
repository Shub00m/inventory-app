import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Connect to SQLite Database
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()



# Create Products Table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price REAL NOT NULL,
                    quantity INTEGER NOT NULL,
                    category TEXT
                )''')
conn.commit()
conn.close()

# Tkinter GUI Application
class InventoryManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("E-commerce Inventory Management")
        self.root.geometry("900x600")
        self.root.configure(bg="#f2f2f2")

        # Styling Variables
        self.primary_color = "#3498db"
        self.bg_color = "#f2f2f2"
        self.text_color = "#333"
        self.font_style = ("Arial", 12)
        self.heading_font = ("Arial", 16, "bold")

        # Variables for product details
        self.name_var = StringVar()
        self.price_var = StringVar()
        self.quantity_var = StringVar()
        self.category_var = StringVar()

        # Title Frame
        title = Label(self.root, text="Inventory Management System", font=("Arial", 24, "bold"), bg=self.primary_color, fg="white", pady=10)
        title.pack(fill=X)

        # Create Tabbed Interface
        tab_control = ttk.Notebook(self.root)
        
        # Add Product Tab
        self.add_tab = Frame(tab_control, bg=self.bg_color)
        tab_control.add(self.add_tab, text="Add Product")

        # View Products Tab
        self.view_tab = Frame(tab_control, bg=self.bg_color)
        tab_control.add(self.view_tab, text="View Products")

        # Pack Tabs
        tab_control.pack(expand=1, fill="both")

        # Add Product Form
        Label(self.add_tab, text="Add New Product", font=self.heading_font, bg=self.bg_color, fg=self.text_color).pack(pady=10)
        
        form_frame = Frame(self.add_tab, bg=self.bg_color)
        form_frame.pack(pady=20)

        Label(form_frame, text="Name", font=self.font_style, bg=self.bg_color, fg=self.text_color).grid(row=0, column=0, padx=10, pady=10, sticky=W)
        Entry(form_frame, textvariable=self.name_var, font=self.font_style).grid(row=0, column=1, padx=10, pady=10)

        Label(form_frame, text="Price", font=self.font_style, bg=self.bg_color, fg=self.text_color).grid(row=1, column=0, padx=10, pady=10, sticky=W)
        Entry(form_frame, textvariable=self.price_var, font=self.font_style).grid(row=1, column=1, padx=10, pady=10)

        Label(form_frame, text="Quantity", font=self.font_style, bg=self.bg_color, fg=self.text_color).grid(row=2, column=0, padx=10, pady=10, sticky=W)
        Entry(form_frame, textvariable=self.quantity_var, font=self.font_style).grid(row=2, column=1, padx=10, pady=10)

        Label(form_frame, text="Category", font=self.font_style, bg=self.bg_color, fg=self.text_color).grid(row=3, column=0, padx=10, pady=10, sticky=W)
        Entry(form_frame, textvariable=self.category_var, font=self.font_style).grid(row=3, column=1, padx=10, pady=10)

        Button(form_frame, text="Add Product", command=self.add_product, bg=self.primary_color, fg="white", font=self.font_style).grid(row=4, columnspan=2, pady=20)

        # View Products Table
        Label(self.view_tab, text="Product Inventory", font=self.heading_font, bg=self.bg_color, fg=self.text_color).pack(pady=10)
        
        self.product_tree = ttk.Treeview(self.view_tab, columns=("ID", "Name", "Price", "Quantity", "Category"), show="headings")
        self.product_tree.heading("ID", text="ID")
        self.product_tree.heading("Name", text="Name")
        self.product_tree.heading("Price", text="Price")
        self.product_tree.heading("Quantity", text="Quantity")
        self.product_tree.heading("Category", text="Category")
        
        self.product_tree.pack(pady=10, fill=BOTH, expand=True)

        # Button Frame
        btn_frame = Frame(self.view_tab, bg=self.bg_color)
        btn_frame.pack(pady=10)

        Button(btn_frame, text="View All Products", command=self.view_products, bg=self.primary_color, fg="white", font=self.font_style).grid(row=0, column=0, padx=5)
        Button(btn_frame, text="Delete Product", command=self.delete_product, bg="#e74c3c", fg="white", font=self.font_style).grid(row=0, column=1, padx=5)

        # Populate product list initially
        self.view_products()

    def add_product(self):
        name = self.name_var.get()
        price = self.price_var.get()
        quantity = self.quantity_var.get()
        category = self.category_var.get()

        # Validate inputs
        if not (name and price and quantity):
            messagebox.showerror("Input Error", "Please fill in all required fields.")
            return

        # Insert into database
        conn = sqlite3.connect('ecommerce.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Products (name, price, quantity, category) VALUES (?, ?, ?, ?)",
                       (name, float(price), int(quantity), category))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Product added successfully!")
        self.clear_inputs()
        self.view_products()

    def view_products(self):
        # Clear existing records
        for item in self.product_tree.get_children():
            self.product_tree.delete(item)

        # Fetch data from database
        conn = sqlite3.connect('ecommerce.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            self.product_tree.insert("", "end", values=row)
        conn.close()

    def delete_product(self):
        try:
            selected_item = self.product_tree.selection()[0]
            product_id = self.product_tree.item(selected_item)['values'][0]

            conn = sqlite3.connect('ecommerce.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Products WHERE id = ?", (product_id,))
            conn.commit()
            conn.close()

            self.product_tree.delete(selected_item)
            messagebox.showinfo("Success", "Product deleted successfully!")

        except IndexError:
            messagebox.showerror("Selection Error", "Please select a product to delete.")

    def clear_inputs(self):
        self.name_var.set("")
        self.price_var.set("")
        self.quantity_var.set("")
        self.category_var.set("")


# Main loop
if __name__ == "__main__":
    root = Tk()
    app = InventoryManagement(root)
    root.mainloop()
