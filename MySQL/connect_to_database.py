import pymysql.cursors

from config import host, user, password, db_name

try:
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Connected successfully")

    # with connection.cursor() as cursor:
    #     select_tables_query = "SHOW TABLES;"
    #     cursor.execute(select_tables_query)
    #     result = cursor.fetchall()
    #     for table in result:
    #         for k, v in table.items():
    #             print(v)
    #
    # with connection.cursor() as cursor:
    #     select_data_query = "SELECT * FROM `users`;"
    #     cursor.execute(select_data_query)
    #     rows = cursor.fetchall()
    #     for row in rows:
    #         print(row)

    # with connection.cursor() as cursor:
    #     crete_table_query = "CREATE TABLE `menu` (" \
    #                         "`id` int AUTO_INCREMENT," \
    #                         "`name` varchar(32)," \
    #                         "`password` varchar(32)," \
    #                         "PRIMARY KEY (`id`));"
    #     cursor.execute(crete_table_query)


except Exception as ex:
    print("Connected refused...")
    print(ex)
