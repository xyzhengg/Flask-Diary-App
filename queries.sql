DELETE FROM users WHERE id = 6;
DELETE FROM users WHERE id = 7;

UPDATE entries SET post_time = '2023-03-03 12:00:00.00' WHERE id=4;
UPDATE entries SET post_time = '2023-03-02 12:00:00.00' WHERE id =2;

SELECT first_name FROM users
INNER JOIN users ON users.id = entries.user_id
;

DELETE FROM entries WHERE id >= 39 AND id < 41;

ALTER TABLE entries DROP COLUMN img_url;