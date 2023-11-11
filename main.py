import sqlite3


con = sqlite3.connect("database.db") 
cur = con.cursor()

""" cur.execute('''CREATE TABLE users
            (id INTEGER NOT NULL,
            name TEXT NOT NULL,
            username TEXT NOT NULL,
            hash TEXT NOT NULL,
            PRIMARY KEY(id)) ''')

cur.execute("CREATE UNIQUE INDEX username ON users(username)") """


""" cur.execute('''CREATE TABLE posts 
            (post_id INTEGER NOT NULL,
            username TEXT NOT NULL,
            post TEXT NOT NULL,
            post_time DATETIME,
            PRIMARY KEY(post_id))''') """
""" cur.execute('''ALTER TABLE posts ADD name TEXT NOT NULL ''') """

""" cur.execute("CREATE UNIQUE INDEX post ON posts(post)") """

""" cur.execute('''CREATE TABLE likes 
            (user_id INTEGER NOT NULL,
            post_id INTEGER NOT NULL)''') """



cur.execute('DELETE FROM posts WHERE post_id IN (10, 11) ')

""" cur.execute('ALTER TABLE posts ADD likes INTEGER') """
""" cur.execute('UPDATE posts SET likes = 0') """
cur.execute('DELETE FROM posts WHERE post_id IN (2,3,4)')
res=cur.execute('SELECT * FROM posts')
for i in res:
    print(i)

con.commit()