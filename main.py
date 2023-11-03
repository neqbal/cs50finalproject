import sqlite3


con = sqlite3.connect("database.db")
cur = con.cursor()


""" cur.execute('''CREATE TABLE users
            (id INTEGER NOT NULL,
            username TEXT NOT NULL,
            hash TEXT NOT NULL,
            PRIMARY KEY(id)) ''') """

""" cur.execute("CREATE UNIQUE INDEX username ON users(username)") """


""" cur.execute('''CREATE TABLE posts 
            (id INTEGER NOT NULL,
            post TEXT NOT NULL,
            uploaded DATETIME)''') """

""" cur.execute('''ALTER TABLE posts ADD username TEXT ''') """

cur.execute('DELETE FROM posts WHERE username = "Joe Biden" ')
con.commit()

res=cur.execute('SELECT * FROM posts')
for i in res:
    print(i)