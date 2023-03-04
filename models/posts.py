import db

def add_entry(diary_code, user_id, diary_heading, diary_text, img_url):
    db.sql_write(
        'INSERT INTO entries (diary_code, user_id, diary_heading, diary_text, img_url) VALUES (%s, %s, %s, %s, %s)',
        [diary_code, user_id, diary_heading, diary_text, img_url]
    )

def get_all_posts():
    all_posts = db.sql_select(
        'SELECT * FROM entries ORDER BY post_time DESC'
    ) 
    return all_posts