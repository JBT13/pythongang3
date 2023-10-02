CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255),
    pageNumber INTEGER,
    DDC VARCHAR(255)
) 

INSERT INTO books (title, pageNumber, DDC) VALUES
('The hobbit', 25 ,'823/.92')
