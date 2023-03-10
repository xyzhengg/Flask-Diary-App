import psycopg2
from psycopg2.extras import RealDictCursor, execute_values

def sql_select(query, params=None):
    db_connection = psycopg2.connect("dbname=flaskdiary")
    db_cursor = db_connection.cursor(cursor_factory=RealDictCursor)

    if params is None:
        db_cursor.execute(query)
    else:
        db_cursor.execute(query, params)
    results = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()
    return results

def sql_select_one(query, params):
    db_connection = psycopg2.connect("dbname=flaskdiary")
    db_cursor = db_connection.cursor(cursor_factory=RealDictCursor)
    db_cursor.execute(query, params)

    result = db_cursor.fetchone()
    db_cursor.close()
    db_connection.close()
    return result


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

def sql_write_return(query, params):
    db_connection = psycopg2.connect("dbname=flaskdiary")
    db_cursor = db_connection.cursor(cursor_factory=RealDictCursor)
    db_cursor.execute(
        query,
        params
    )
    db_connection.commit()
    result = db_cursor.fetchone()
    db_cursor.close()
    db_connection.close()
    return result

def sql_write_many(query, params):
    db_connection = psycopg2.connect("dbname=flaskdiary")
    db_cursor = db_connection.cursor(cursor_factory=RealDictCursor)
    execute_values (
        db_cursor,
        query,
        params
    )
    db_connection.commit()
    db_cursor.close()
    db_connection.close()
