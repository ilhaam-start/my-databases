
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS post_id_seq;

DROP TABLE IF EXISTS user_accounts;
DROP SEQUENCE IF EXISTS user_accounts_id_seq;

CREATE SEQUENCE IF NOT EXISTS user_accounts_id_seq;
CREATE TABLE user_accounts (
    id SERIAL PRIMARY KEY,
    email_address text,
    username text
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    views int,
    user_account_id int,
    constraint fk_user_account foreign key(user_account_id)
        references user_accounts(id)
        on delete cascade
);

INSERT INTO user_accounts (email_address, username) VALUES ('ilhaam777@gmail.com', 'ilhaam777');
INSERT INTO user_accounts (email_address, username) VALUES ('ilhaam.ahmed@hotmail.com', 'ilhaam1');
INSERT INTO user_accounts (email_address, username) VALUES ('ahmed@gmail.com', 'illy');
INSERT INTO user_accounts (email_address, username) VALUES ('il.ah@gmail.com', 'ilham');

INSERT INTO posts (title, content, views, user_account_id) VALUES ('title1', 'content1', 5, 1);
INSERT INTO posts (title, content, views, user_account_id) VALUES ('title2', 'content2', 15, 2);
INSERT INTO posts (title, content, views, user_account_id) VALUES ('title3', 'content3', 56, 3);
INSERT INTO posts (title, content, views, user_account_id) VALUES ('title4', 'content4', 3, 4);
INSERT INTO posts (title, content, views, user_account_id) VALUES ('title5', 'content5', 100, 3);