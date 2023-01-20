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

    # with connection.cursor() as cursor:
    #     query = """
    #                 CREATE TABLE tags (
    #                 id serial PRIMARY KEY,
    #                 tag_name varchar(50) NOT NULL
    #                 );
    #             """
    #     cursor.execute(query)
    #     print("Table tag created")

    # with connection.cursor() as cursor:
    #
    #     query = """
    #                 CREATE TABLE posts_tags (
    #                 post_id int REFERENCES posts(id),
    #                 tag_id int REFERENCES tags(id),
    #                 CONSTRAINT posts_tags_fk PRIMARY KEY (post_id, tag_id)
    #                 );
    #             """
    #     cursor.execute(query)
    #     print("Table posts_tags created")

    # with connection.cursor() as cursor:
    #     tags = ['Python', 'MySQL', 'Java', 'PostgreSQL', 'Django']
    #     for tag in tags:
    #         query = f"""
    #                     INSERT INTO tags (tag_name)
    #                     VALUES ('{tag}');
    #                 """
    #         cursor.execute(query)

    # with connection.cursor() as cursor:
    #     query = """
    #                 INSERT INTO posts_tags VALUES (1, 1), (2, 2), (2, 3), (3, 1), (3, 4), (3, 5);
    #             """
    #     cursor.execute(query)
    #     print("Insert data to posts_tags")

    # with connection.cursor() as cursor:
    #     query = """ SELECT * FROM tags """
    #     cursor.execute(query)
    #     mytable = from_db_cursor(cursor)
    #     print(mytable)

    # with connection.cursor() as cursor:
    #     query = """
    #                 SELECT * FROM posts_tags;
    #             """
    #     cursor.execute(query)
    #     mytable = from_db_cursor(cursor)
    #     print(mytable)

    # with connection.cursor() as cursor:
    #     query = """DELETE FROM tags WHERE id > 5;"""
    #     cursor.execute(query)
    #     print("Successfully...")

    with connection.cursor() as cursor:
        query = """
                    SELECT posts.id, posts.post_title, tags.tag_name FROM posts
                    LEFT JOIN posts_tags ON posts.id = posts_tags.post_id
                    LEFT JOIN tags ON posts_tags.tag_id = tags.id;
                """
        cursor.execute(query)
        mytable = from_db_cursor(cursor)
        print(mytable)


except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print(f"[INFO] PostgreSQL connection closed")