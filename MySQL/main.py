import pymysql.cursors

from config import host, user, password, db_name


try:
    connection = pymysql.connect(
        host=host,
        user=user,
        port=3306,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("=" * 30)
    print("successfully connected ...".center(30))
    print("=" * 30)

    try:
        # with connection.cursor() as cursor:
            # cursor.execute("SHOW DATABASES;")
            # print(cursor.fetchall())

            # cursor.execute("SHOW TABLES;")
            # print(cursor.fetchall())

            # drop_table = "DROP TABLE `test_db`;"
            # cursor.execute(drop_table)

        # with connection.cursor() as cursor:

            # create_table_query = """CREATE TABLE `customers`(
            #                         `id` int(11) AUTO_INCREMENT,
            #                         `name` varchar(32),
            #                         `password` varchar(32),
            #                         `email` varchar(32),
            #                         PRIMARY KEY (`id`)
            #                         );"""
            # cursor.execute(create_table_query)
            # print("Table created successfully")

            # create_table_query = """CREATE TABLE `users` (
            #                         `id` int(11) NOT NULL AUTO_INCREMENT,
            #                         `email` varchar(255) COLLATE utf8_bin NOT NULL,
            #                         `password` varchar(255) COLLATE utf8_bin NOT NULL,
            #                         PRIMARY KEY (`id`)
            #                         );"""
            # cursor.execute(create_table_query)
            # print("Table created successfully")

        # with connection.cursor() as cursor:

            # insert_query = """INSERT INTO `customers` (name, password, email)
            #                   VALUES ('Serhii', 'qwerty', 'serhii@gmail.com');"""
            # cursor.execute(insert_query)
            # connection.commit()

        # with connection.cursor() as cursor:

            # update_query = "UPDATE `customers` SET name = 'Oleg' WHERE id = 1;"
            # cursor.execute(update_query)
            # connection.commit()

        # with connection.cursor() as cursor:

            # delete_query = "DELETE FROM `my_users` WHERE id = 3;"
            # cursor.execute(delete_query)
            # connection.commit()

        # with connection.cursor() as cursor:
        #
        #     select_all_rows = "SELECT * FROM `customers`"
        #     cursor.execute(select_all_rows)
        #     rows = cursor.fetchall()
        #     for row in rows:
        #         print(row)

        # with connection.cursor() as cursor:
        #
        #     select_all_rows = "SELECT * FROM `users`"
        #     cursor.execute(select_all_rows)
        #     rows = cursor.fetchall()
        #     for row in rows:
        #         print(row)

    finally:
        connection.close()

except Exception as ex:
    print("Connection refused ...")
    print(ex)

