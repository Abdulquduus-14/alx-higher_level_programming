-- a script that creates a table second_table in the database hbtn_0c_0
-- in your MySQL server and add multiples rows.
CREATE TABLE hbtn_0c_0.second_table (id INT, name VARCHAR(256), score INT);
INSERT INTO hbtn_0c_0.second_table
VALUES (1, "john", 10)
VALUES (2, "Alex", 3)
VALUES (3, "Bob", 14)
VALUES (4, "George", 8);
