import sqlite3

#Method to connect to db and create table book and create the table schema
def connect():
    #Create connection object ot db
    conn=sqlite3.connect("books.db")
    #Now create the cursor object -that we will use to execute the sql query
    cur=conn.cursor()
    #Now call the execute function on the cursor object(This from the sqlite3 class)
    cur.execute("CREATE TABLE IF NOT EXISTS book (id integer PRIMARY KEY,title text,author text,year integer,isbn integer)")
    #Now commit the sql query to db engine for execution
    conn.commit()
    #Close the sql connection on conn object
    conn.close()

def insert(title,author,year,isbn):
    #Function to insert data insto SQLITE3 db
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    #Input the SQL query to execute on the db/table here
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()


def search(title="",author="",year="",isbn=""):
    #Search function to find relevant Entry
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    #Input the SQL query to execute on the db/table here
    cur.execute("SELECT * from book where title=? OR author=? or year=? or isbn=?",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def viewall():
    #To view all data in db
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * from book")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(title,author,year,isbn):
    #Function to delete an records
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    #Input the SQL query to execute on the db/table here
    conn.commit()
    conn.close()

def close():
    #close the tkinter window
    pass


#Connect to the sqlite3 db and create the table book - with the relevant schema.
connect()
insert("The sea","Henry Morrin", 1918,19312812)
print(viewall())
print(search("Henry Morrin"))
