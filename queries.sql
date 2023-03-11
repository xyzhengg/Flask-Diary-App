DELETE FROM users WHERE id = 6;
DELETE FROM users WHERE id > 7;

UPDATE entries SET post_time = '2023-03-03 12:00:00.00' WHERE id=4;
UPDATE entries SET post_time = '2023-03-02 12:00:00.00' WHERE id =2;

SELECT first_name FROM users
INNER JOIN users ON users.id = entries.user_id
;

DELETE FROM entries WHERE id >= 39 AND id < 41;

ALTER TABLE entries DROP COLUMN img_url;

ALTER TABLE messages ADD COLUMN post_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP(2);
ALTER TABLE messages ADD COLUMN diary_code VARCHAR(8) NOT NULL;

DELETE FROM entries WHERE user_id = 4;
DELETE FROM entries WHERE user_id = 29;

DELETE FROM messages WHERE user_id = 29;
DELETE FROM messages WHERE user_id = 4;

DELETE FROM images WHERE entry_id IN (SELECT id FROM entries WHERE user_id = 29);
DELETE FROM images WHERE entry_id IN (SELECT id FROM entries WHERE user_id = 4);

DELETE FROM users WHERE id =35;


DELETE FROM diary WHERE id =30;

DELETE email_2 from diary WHERE email_2 = fluffy@heyhey.com;