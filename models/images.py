import db

def insert_images(query, params): 
    db.sql_write(
        f'INSERT INTO images (public_id, img_url, entry_id) VALUES {", " .join(placeholders)}',
        [params]
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