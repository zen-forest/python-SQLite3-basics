import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS tshirts 
                (sku text, name text, size text, price real)''')

cur.execute('''INSERT INTO tshirts VALUES
                ('SKU234234', 'Black logo tshirt', 'Medium', '24.00')''')

con.commit()

for row in cur.execute('''SELECT * FROM tshirts'''):
  print(row)

# Questions
# Why is the word cursor used? 