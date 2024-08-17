from pdf_engine import createpdf
import pyodbc

client = input("Ingrese el nombre del cliente: ")
path = r"D:\Users\Sergio Moy\Documents\Database1.accdb"
conn_str = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + path + ';'
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

orden = [["Producto", "Peso", "Precio", "Cantidad"]]
id = input("Ingrese el producto a agregar a la cotización: ")

while id !="-1":
    query = f'SELECT * from Productos where ID = ?'
    cursor.execute(query, (id,))
    record = cursor.fetchone()
    quant = int(input("Ingrese la cantidad a comprar: "))
    orden.append([record[1], record[2], record[3], quant])
    id = input("Ingrese el producto a agregar a la cotización: ")
cursor.close()
conn.close()

print(orden)

createpdf(client, orden, 1)