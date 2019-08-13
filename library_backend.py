import sqlite3

# Creating database file if file not previously present and open if present already
def connect():
    conn=sqlite3.connect("library.db")
    cur=conn.cursor()
    # Adding sql commands
    cur.execute("CREATE TABLE IF NOT EXISTs library (id INTEGER PRIMARY KEY , name TEXT , card INTEGER , mobile INTEGER , book TEXT , issue INTEGER , issued INTEGER)")
    conn.commit()
    conn.close()

# Inserting elements to the database
def insert(name,card,mobile,book,issue,issued):
    conn=sqlite3.connect("library.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO library VALUES (NULL, ?,?,?,?,?,?)",(name,card,mobile,book,issue,issued))
    conn.commit()
    conn.close()
    view()

# To view all entries made
def view():
    conn=sqlite3.connect("library.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM library")
    row=cur.fetchall()
    conn.close()
    return row

#  For searching entries
def search(name="",card="",mobile="",book="",issue="",issued=""):
    conn=sqlite3.connect("library.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM library WHERE name=? OR card=? OR mobile=? OR book=? OR issue=? OR issued=?",(name,card,mobile,book,issue,issued))
    row=cur.fetchall()
    conn.close()
    return row

# Deleting entry
def delete(id):
    conn=sqlite3.connect("library.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM library WHERE id=?",(id))
    conn.commit()
    conn.close()

# Updating entries
def update(id,name,card,mobile,book,issue,issued):
    conn=sqlite3.connect("library.db")
    cur=conn.cursor()
    cur.execute("UPDATE library SET name=?,card=? ,mobile=? ,book=? ,issue=? ,issued=? WHERE id=?",(name,card,mobile,book,issue,issued))
    conn.commit()
    conn.close()

connect()