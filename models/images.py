import db

def insert_many_images(image_rows): 
    db.sql_write_many(
        'INSERT INTO images (public_id, img_url, entry_id) VALUES %s',
        image_rows
    )

def get_all_images(post_id):
    data = db.sql_select(
        'SELECT * FROM images WHERE entry_id = %s', [post_id]
    )
    return data

def delete_all_images(post_id):
    db.sql_write (
        'DELETE FROM images WHERE entry_id=%s',
        [post_id]
    )

