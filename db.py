import pyodbc

def buscarproducto(nombre, cursor):
    query = 'SELECT * FROM Productos WHERE Descripcion LIKE ?'
    cursor.execute(query, ('%'+nombre+'%'))
    record = cursor.fetchall()
    return record

def buscarproveedor(nombre, cursor):
    query = 'SELECT * FROM Proveedor WHERE NAME_Prov LIKE ?'
    cursor.execute(query, ('%'+nombre+'%'))
    record = cursor.fetchall()
    return record

def crearproducto(desc, peso, partnumber, marca, partnumberoem, marcaoem, uso, cursor, conn):
    data = (desc, peso, partnumber, marca, partnumberoem, marcaoem, uso)
    query = 'INSERT INTO Productos (Descripcion, [Peso (Kg)], [Part Number - Marca], Marca, [Part-Number_OEM], Marca_OEM, USO) VALUES (?, ?, ?, ?, ?, ?, ?);'
    cursor.execute(query, data)
    conn.commit()

def borrarproducto(id, cursor, conn):
    query = 'DELETE FROM Productos WHERE id = ?'
    cursor.execute(query, id)
    conn.commit()

def modificarproducto(id,desc, peso, partnumber, marca, partnumberoem, marcaoem, uso, cursor, conn):
    data = (desc, peso, partnumber, marca, partnumberoem, marcaoem, uso, id)

    query = '''
    UPDATE Productos x
    SET Descripcion = ?, [Peso (Kg)] = ?, [Part Number - Marca] = ?, Marca = ?, [Part-Number_OEM] = ?, Marca_OEM = ?, USO = ? 
    WHERE ID = ?;
    '''

    cursor.execute(query, data)
    conn.commit()


file = open('dbname.txt')
nombre = file.readlines()[0]
file.close()
path = rf".\{nombre}"

conn_str = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + path + ';'
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
conn.setdecoding(pyodbc.SQL_CHAR, encoding='latin1')
conn.setencoding('latin1')
modificarproducto(18, "Producto de prueba - modificado", 15, "0x36", 2, "6", 1, "N/A", cursor, conn)

cursor.close()
conn.close()