import sqlite3

db = sqlite3.connect('books.db')

cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS books(
  id integer PRIMARY KEY,
  title text NOT NULL,
  author text NOT NULL,
  price real);''')

book_list = [
  ('2','Animal Farm','George Orwell','7.49'),
  ('3','The Power of Now','Eckhart Tolle','7.49'),
  ('4','Mans Search For Meaning','Viktor Frankl','7.49'),
  ('5','The Design of Everyday Things','Don Norman','7.49'),
] 

cur.executemany('''INSERT INTO books(id, title, author, price) values(?,?,?,?)
''', book_list)

db.commit()
db.close()  