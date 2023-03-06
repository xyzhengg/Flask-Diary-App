import db

def add_entry(diary_code, user_id, diary_heading, diary_text, img_url):
    db.sql_write(
        'INSERT INTO entries (diary_code, user_id, diary_heading, diary_text, img_url) VALUES (%s, %s, %s, %s, %s)',
        [diary_code, user_id, diary_heading, diary_text, img_url]
    )

def get_all_posts(diary_id):
    data = db.sql_select(
        'SELECT * FROM entries WHERE diary_code = %s ORDER BY post_time DESC', [diary_id]
    ) 
    return data

def get_single_post(post_id):
    data = db.sql_select_one(
        'SELECT * FROM entries WHERE id = %s', [post_id]
    )
    return data

def edit_entry(new_heading, new_text, new_img, fav, new_timedate, post_id):
    db.sql_write (
        'UPDATE entries SET diary_heading=%s, diary_text=%s, img_url=%s, fav=%s, post_time=%s WHERE id=%s',
        [new_heading, new_text, new_img, fav, new_timedate, post_id]
    )