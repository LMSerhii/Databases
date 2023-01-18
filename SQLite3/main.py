import sqlite3

connection = sqlite3.connect('test.db')

with connection:
    connection.execute("""
                       CREATE TABLE USER (
                           id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                           name TEXT,
                           age INTEGER
                       );
                       """)

sql_query = 'INSERT INTO USER (id, name, age) values (?, ?, ?)'
data = [
    (1, 'Joni', 21),
    (2, 'Andrew', 34),
    (3, 'Nikolas', 28)
]
with connection:
    connection.executemany(sql_query, data)

with connection:
    rows = connection.execute("SELECT * FROM USER WHERE age <= 22")
    for row in rows:
        print(row)
    