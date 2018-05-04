import sqlite3

def create_table():
    connector = sqlite3.connect("bookstore.db")
    cursor = connector.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, titulo TEXT, autor TEXT, ano INTEGER, isbn INTEGER)")
    connector.commit()
    connector.close()



def addbook(titulo, autor, ano, isbn):
    connector = sqlite3.connect("bookstore.db")
    cursor = connector.cursor()
    cursor.execute("INSERT INTO books VALUES(NULL,?,?,?,?)", (titulo, autor, ano, isbn))
    connector.commit()
    connector.close()


def view():
    connector = sqlite3.connect("bookstore.db")
    cursor = connector.cursor()
    cursor.execute("SELECT * FROM books")
    rows=cursor.fetchall()
    connector.close()
    return(rows)


def search(titulo="", autor="", ano="", isbn=""):
    connector = sqlite3.connect("bookstore.db")
    cursor = connector.cursor()
    cursor.execute("SELECT * FROM books WHERE titulo =? OR autor =? OR ano =? OR isbn =?", (titulo, autor, ano, isbn))
    rows = cursor.fetchall()
    connector.close()
    return(rows)


def delete(id):
    connector = sqlite3.connect("bookstore.db")
    cursor = connector.cursor()
    cursor.execute("DELETE FROM books WHERE id =?", (id,))
    connector.commit()
    connector.close()


def update(id, titulo, autor, ano, isbn):
    connector = sqlite3.connect("bookstore.db")
    cursor = connector.cursor()
    cursor.execute("UPDATE books SET titulo=?, autor=?, ano=?, isbn=? WHERE id=?", (titulo, autor, ano, isbn, id))
    connector.commit()
    connector.close()
