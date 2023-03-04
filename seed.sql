INSERT INTO users (first_name, last_name, email, password_hash, diary_code) VALUES 
('xin', 'zheng', 'xin@heyhey.com', 'sha256:260000$D3p1AcCj9ZLCiu17$9f5bd8b00ad1bbd0b7d2df41986752262ba2412fcecc7c3b0bceac6735644c5c', 'PHP31Q3V');

INSERT INTO users (first_name, last_name, email, password_hash, diary_code) VALUES 
('johnny', 'chan', 'johnny@heyhey.com', 'sha256:260000$D3p1AcCj9ZLCiu17$9f5bd8b00ad1bbd0b7d2df41986752262ba2412fcecc7c3b0bceac6735644c5c', 'PHP31Q3V');

INSERT INTO diary (diary_code, email_1, email_2) VALUES
('PHP31Q3V', 'xin@heyhey.com', 'johnny@heyhey.com');

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(25) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password_hash TEXT NOT NULL,
    diary_code VARCHAR(8)
);

CREATE TABLE diary (
    id SERIAL PRIMARY KEY,
    diary_code VARCHAR(8) NOT NULL,
    email_1 VARCHAR(50) NOT NULL,
    email_2 VARCHAR(50)
);

CREATE TABLE entries (
    id SERIAL PRIMARY KEY,
    diary_code VARCHAR(8) NOT NULL,
    user_id INT NOT NULL,
    diary_heading VARCHAR(25),
    diary_text TEXT,
    img_url TEXT,
    fav BOOLEAN,
    post_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP(2)
    );