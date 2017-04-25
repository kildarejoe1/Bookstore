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
    cur.execute("SELECT * from book where title=? OR author=? or year=? or isbn=?",(title,author,year,isbn))#String formatting/string substition
    rows=cur.fetchall()#Fetch all the sql results from the sql execute command
    conn.close() #close the sqlite3 connection - notice no commit here- as just receiving data
    return rows

def viewall():
    #To view all data in db
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * from book")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    #Function to delete an records
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    #Input the SQL query to execute on the db/table here
    cur.execute("DELETE FROM book WHERE ID=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    #Input the SQL query to execute on the db/table here
    cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? where id=?"(title,author,year,isbn))
    conn.commit()
    conn.close()

def close():
    #close the tkinter window
    pass


#Connect to the sqlite3 db and create the table book - with the relevant schema.
"""
insert("The Princess","Lilly Morrin",2012,192345678)
connect()

print(viewall())
"""
