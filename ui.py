import tkinter as tk
from tkinter import ttk
import pyodbc

class ProductApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Product Selection App")
        
        # Create a database connection
        path = r"D:\Users\Sergio Moy\Documents\Database1.accdb"
        conn_str = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + path + ';'
        self.conn = pyodbc.connect(conn_str)
        self.cursor = self.conn.cursor()
        
        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Dropdown menu for product selection
        self.product_var = tk.StringVar()
        self.product_dropdown = ttk.Combobox(self.root, textvariable=self.product_var)
        self.product_dropdown.pack(pady=10)
        
        # Load products into the dropdown
        self.load_products()
        
        # Button to add selected product to the table
        self.add_button = tk.Button(self.root, text="Add to Table", command=self.add_to_table)
        self.add_button.pack(pady=5)
        
        # Treeview for displaying products
        self.table = ttk.Treeview(self.root, columns=('Product',), show='headings')
        self.table.heading('Product', text='Product')
        self.table.pack(pady=10)
        
    def load_products(self):
        # Fetch product names from the database
        self.cursor.execute("SELECT Nombre FROM Productos")
        products = self.cursor.fetchall()
        
        # Update the dropdown menu with products
        product_names = [product[0] for product in products]
        self.product_dropdown['values'] = product_names

    def add_to_table(self):
        # Get selected product
        selected_product = self.product_var.get()
        
        if selected_product:
            # Insert the selected product into the table
            self.table.insert('', 'end', values=(selected_product,))
        else:
            print("No product selected")

    def __del__(self):
        # Close the database connection when the app is closed
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = ProductApp(root)
    root.mainloop()
