import psycopg2
from prettytable import PrettyTable, from_db_cursor

from config import host, user, password, db_name

mytable = PrettyTable()
try:
    # connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    # connection.autocommit = True
    
    # the cursor for performing database operations
    with connection.cursor() as cursor:

        sql_query = "SELECT version();"
        cursor.execute(sql_query)
        print(f"Server version: {cursor.fetchone()}")

        query = """SELECT pg_database_size(current_database());"""
        cursor.execute(query)
        # print(f"Current database size: {cursor.fetchone()[0]}")
        mytable = from_db_cursor(cursor)
        print(mytable)

        query = """SELECT pg_size_pretty(pg_database_size(current_database()));"""
        cursor.execute(query)
        print(f"Current database size: {cursor.fetchone()[0]}")

        print("SHOW TABLES".center(100, "-"))
        show_table_query = """
                                SELECT table_name FROM information_schema.tables
                                WHERE table_schema NOT IN ('information_schema','pg_catalog');
                           """
        cursor.execute(show_table_query)
        # print(cursor.fetchall())
        mytable = from_db_cursor(cursor)
        print(mytable)
        print("-" * 100)

        # # -------------------- create table ------------------------
        # create_table_query = """
        #                         CREATE TABLE pizzas (
        #                         id serial PRIMARY KEY,
        #                         pizzas_name varchar(30) NOT NULL
        #                         );
        #                      """
        # cursor.execute(create_table_query)
        # connection.commit()
        # print("Table created successfully")

        # -------------------- drop table ------------------------
        # cursor.execute("""DROP TABLE pizzas;""")
        # connection.commit()
        # print("Table dropped successfully!")

        # -------------------- insert data in table ------------------------

        # insert_data_query = """
        #                         INSERT INTO pizzas (pizzas_name)
        #                         VALUES ('Four cheese');
        #                     """
        # cursor.execute(insert_data_query)
        # connection.commit()
        # print("Insert data was successfully")

        # -------------------- select data -------------------------------
        # select_data_query = "SELECT * FROM pizzas;"
        # cursor.execute(select_data_query)
        # print(cursor.fetchall())

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print(f"[INFO] PostgreSQL connection closed")