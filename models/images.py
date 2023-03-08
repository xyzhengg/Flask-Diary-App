import db

def insert_images(params, placeholders): 
    db.sql_write(
        f'INSERT INTO images (public_id, img_url, entry_id) VALUES {", " .join(placeholders)}',
        [params]
    )
