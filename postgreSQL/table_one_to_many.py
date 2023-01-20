import psycopg2

from prettytable import from_db_cursor

from config import host, user, password, db_name


try:
    # connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    # the cursor for performing database operations
    with connection.cursor() as cursor:

        # -------------------- create table one to many -----------
        # create_first_table_query = """
        #                                 CREATE TABLE categories (
        #                                 id serial PRIMARY KEY,
        #                                 post_categories varchar(50)
        #                                 );
        #                             """
        # cursor.execute(create_first_table_query)
        # print("Table created successfully!")
        #
        # create_second_table_query = """
        #                                 CREATE TABLE posts (
        #                                 id serial PRIMARY KEY,
        #                                 post_title varchar(150) NOT NULL,
        #                                 post_text text NOT NULL,
        #                                 fk_posts_categories int REFERENCES categories(id)
        #                                 );
        #                             """
        # cursor.execute(create_second_table_query)
        # print("Table created successfully!")

        # sql_insert_query = """
        #                         INSERT INTO categories (post_categories) VALUES ('sport');
        #                    """
        # cursor.execute(sql_insert_query)
        # print("Successfully...")

        # sql_insert = """
        #                 INSERT INTO posts (post_title, post_text, fk_posts_categories)
        #                 VALUES (
        #                 'post_7',
        #                 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,
        #                 sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        #                 Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
        #                 nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
        #                 reprehenderit in voluptate velit esse cillum dolore eu
        #                 fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
        #                 sunt in culpa qui officia deserunt mollit anim id est laborum.',
        #                 1)
        #             """
        # cursor.execute(sql_insert)

        # sql_select = """
        #                 SELECT categories.post_categories FROM categories;
        #             """
        # cursor.execute(sql_select)
        # # print(cursor.fetchall())
        # res = cursor.fetchall()
        # for row in res:
        #     # print(row)
        #     for el in row:
        #         print(el)

        # query = """
        #             SELECT * FROM posts;
        #         """
        # cursor.execute(query)
        # # print(cursor.fetchall())
        # for row in cursor.fetchall():
        #     print(row)

        query = """
                    SELECT posts.*, categories.post_categories FROM posts INNER JOIN categories ON 
                    categories.id = posts.fk_posts_categories;
                """
        cursor.execute(query)
        # for row in cursor.fetchall():
        #     print(row)
        mytable = from_db_cursor(cursor)
        print(mytable)

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print(f"[INFO] PostgreSQL connection closed")