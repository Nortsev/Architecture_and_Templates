import sqlite3

con = sqlite3.connect('base_sql.sqlite')
cur = con.cursor()
with open('create_db.sql', 'r') as f:
    text = f.read()
cur.executescript(text)
cur.close()
con.close()
