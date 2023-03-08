import db

def sql_write(query, params):
    db_connection = psycopg2.connect("dbname=flaskdiary")
    db_cursor = db_connection.cursor(cursor_factory=RealDictCursor)
    db_cursor.execute(
        query,
        params
    )
    db_connection.commit()
    db_cursor.close()
    db_connection.close()


def insert_images(params): 
    db.sql_write(
        f'INSERT INTO images (public_id, img_url, entry_id) VALUES {', '.join(placeholders)}',
        [params]
    )
