import sqlite3

def crear_bd():
    con=sqlite3.connect('menu.db')
    cursor=con.cursor()
    try:
        cursor.execute("CREATE TABLE categoria (id INTEGER PRIMARY KEY AUTOINCREMENT,"+
        "nombre varchar(255) NOT NULL)")
        cursor.execute("CREATE TABLE plato (id INTEGER PRIMARY KEY AUTOINCREMENT,"+
        "nombre VARCHAR(255) UNIQUE NOT NULL, id_categoria INTEGER, FOREIGN KEY(id_categoria) REFERENCES categoria(id))")
    except:
        print('Las tablas no han sido creadas o estan repetidas')
    else:
        con.commit()
        print('Las tablas han sido creadas')
    finally:    
        cursor.close()
        con.close()

def agregar_categoria():
    nueva_categoria=input('Dime el nombre de una nueva categoría: ')
    con=sqlite3.connect('menu.db')
    cursor=con.cursor()
    try:
        cursor.execute("INSERT INTO categoria VALUES (null, '"+nueva_categoria+"')")
    except:
        print('La nueva categoria no ha sido creada o está repetida')
    else:
        con.commit()
        print('La nueva categoría ha sido creada')
    finally:
        cursor.close()
        con.close()

def agregar_plato():
    print('Categorías disponibles')
    print('(1)Primeros')
    print('(2)Segundos')
    print('(3)Postres')
    categoria=input('Escoje una categoría: ')
    plato=input('Dime el nombre del plato: ')
    con=sqlite3.connect('menu.db')
    cursor=con.cursor()
    try:
        cursor.execute("INSERT INTO plato VALUES (null, '"+plato+"', '"+categoria+"')")
    except:
        print('El plato no ha sido introducido')
    else:
        con.commit()
        print('El plato ha sido introducido correctamente')
    finally:
        cursor.close()
        con.close()

def mostrar_menu():
    con=sqlite3.connect('menu.db')
    cursor=con.cursor()
    cursor.execute("SELECT * FROM categoria INNER JOIN plato ON categoria.id=plato.id_categoria")
    categorias=cursor.fetchall()
    i=1
    for categoria in categorias:
        print(str(categoria[1]))
        print(f'{categoria[3]}\n')
        i+=1
    cursor.close()
    con.close()
        