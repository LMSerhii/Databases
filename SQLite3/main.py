import sqlite3

with sqlite3.connect('test.db') as connect:
    cursor = connect.cursor()

    # cursor.execute("""
    #                    CREATE TABLE user (
    #                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    #                        name TEXT,
    #                        age INTEGER
    #                    );
    #                 """)
    # connect.commit()

    # cursor.execute("""
    #         CREATE TABLE articles (
    #         title_article text NOT NULL,
    #         full_text text NOT NULL,
    #         author text NOT NULL)
    # """)
    # connect.commit()

    # sql_query = 'INSERT INTO user (id, name, age) VALUES (?, ?, ?)'
    # data = [
    #     (4, 'Billi', 29),
    #     (5, 'Rebeka', 22),
    #     (6, 'Tomas', 36)
    # ]
    # cursor.executemany(sql_query, data)
    # connect.commit()

    # sql_query = """
    #     INSERT INTO articles VALUES ('moto', 'Awesome text', 'Billi')
    # """

    # cursor.execute(sql_query)
    # connect.commit()

    # cursor.execute("SELECT * FROM user")
    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row)

    # cursor.execute("SELECT * FROM user WHERE age <= 30")
    # # print(cursor.fetchone())
    # # print(cursor.fetchmany(2))
    # rows = cursor.fetchall()
    # print(rows)
    # for row in rows:
    #     print(row)

    cursor.execute("SELECT rowid, * FROM articles")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # cursor.execute("SELECT rowid, * FROM articles WHERE title_article <> 'tech'")
    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row)

    # cursor.execute("SELECT rowid, * FROM articles WHERE title_article = 'tech' ORDER BY rowid DESC")
    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row)

    # delete all rows
    # cursor.execute("""DELETE FROM articles""")

    # cursor.execute("""DELETE FROM articles WHERE rowid = 2""")

    # cursor.execute("""UPDATE articles SET author = 'admin' WHERE title_article = 'tech'""")

    # cursor.execute("""UPDATE articles SET author = 'admin', full_text = 'cool text' WHERE title_article = 'tech'""")
