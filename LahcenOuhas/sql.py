import sqlite3



conn = sqlite3.connect('database.db')

cursor = conn.cursor()
cursor.execute('''CREATE TABLE users
                  (id INT PRIMARY KEY NOT NULL,
                  name TEXT NOT NULL);''')

cursor.execute("INSERT INTO users (id, name) VALUES (1, 'John')")

conn.commit()
