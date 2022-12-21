import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS tshirts 
                (sku text PRIMARY KEY, name text, size text, price real)''')

cur.execute('''INSERT OR IGNORE INTO tshirts VALUES
                ('SKU2342344', 'Black logo tshirt', 'Medium', '24.00')''')

con.commit()

for row in cur.execute('''SELECT * FROM tshirts'''):
  print(row)

# Questions
# Why is the word cursor used? 
# The use of the term "cursor" in this context likely arose because it is a 
# metaphor that is easy to understand and reflects the way the cursor works in many other contexts, such as when it is used to navigate through text in a word processor or to move around the screen in a graphical user interface.
# 
# In database programming, the cursor is often used to iterate through the rows of a result set and perform some operation on each row. 
# For example, you might use a cursor to retrieve the data from each row in a result set, process that data in some way, and then move on to the next row.
# 
# Overall, the use of the term "cursor" in database programming reflects the way that it is used in many other contexts to refer to a pointer or marker that is used to navigate through a set of data.