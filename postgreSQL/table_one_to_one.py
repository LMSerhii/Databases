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

    with connection.cursor() as cursor:

        # create_first_table_query = """
        #                                 CREATE TABLE users (
        #                                 id serial PRIMARY KEY,
        #                                 first_name varchar(50) NOT NULL,
        #                                 last_name varchar(50) NOT NULL
        #                                 );
        #                              """
        # cursor.execute(create_first_table_query)
        # connection.commit()
        # print("Table created successfully!")
        #
        # create_second_table_query = """
        #                                 CREATE TABLE passports (
        #                                 id serial PRIMARY KEY,
        #                                 passport_number int NOT NULL,
        #                                 city_of_registration varchar(50) NOT NULL,
        #                                 fk_passports_users int REFERENCES users(id)
        #                                 );
        #                             """
        # cursor.execute(create_second_table_query)
        # connection.commit()
        # print("Table created successfully!")

        # insert_data_query = """
        #                         INSERT INTO users (first_name, last_name)
        #                         VALUES ('Joni', 'Dred');
        #                     """
        # cursor.execute(insert_data_query)
        # connection.commit()
        # print("Insert data was successfully")
        #
        # insert_data_query = """
        #                         INSERT INTO passports (passport_number, city_of_registration, fk_passports_users)
        #                         VALUES (33333, 'Lviv', 3);
        #                     """
        # cursor.execute(insert_data_query)
        # connection.commit()
        # print("Insert data was successfully")

        # sql_select_query = """ SELECT * FROM users; """
        # cursor.execute(sql_select_query)
        # print(cursor.fetchall())
        #
        # sql_select_query = """ SELECT * FROM passports; """
        # cursor.execute(sql_select_query)
        # print(cursor.fetchall())

        sql_combi_query = """
                                SELECT users.*, passports.passport_number,
                                passports.city_of_registration FROM users, passports 
                                WHERE users.id = passports.fk_passports_users;
                          """
        cursor.execute(sql_combi_query)
        # print(cursor.fetchall())
        mytable = from_db_cursor(cursor)
        print(mytable)

        # cursor.execute("DROP TABLE users;")
        # connection.commit()
        # print("Table dropped successfully")

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print(f"[INFO] PostgreSQL connection closed")
