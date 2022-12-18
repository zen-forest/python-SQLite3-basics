import sqlite3

db = sqlite3.connect('books.db')

cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS books(
  id integer PRIMARY KEY,
  title text NOT NULL,
  author text NOT NULL,
  price real);''')

db.commit()
db.close() 