CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    comment text
);

-- Then the table with the foreign key second.
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    content text,
    author_name text,
    post_id int,
-- The foreign key name is always {other_table_singular}_id
    constraint fk_post foreign key(post_id)
    references posts(id)
    on delete cascade
);