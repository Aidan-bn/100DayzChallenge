CREATE DATBASE Utumishi;

USE DATABASE Utumishi;

CREATE TABLE interview (
    id INT UNSIGNED NOT NULL auto_increment,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    PRIMARY KEY (id) 
);

INSERT INTO interview (username, email) 
    VALUES ('Aidan Banteze', 'bantezea@gmail.com');

UPDATE interview
    SET username = 'Habayo'
    WHERE id = 1;

DESC utumishi.interview;

DESC interview;

CREATE USER 'job'@'localhost' IDENTIFIED BY 'job-search';
-- create user that can connect only in a local machine where database is hosted

CREATE USER 'job-anywhere'@'%' IDENTIFIED BY 'job-anywhere';   
-- create user that can connect any where except in a local machine

-- grant privilleges to a usr for all tables of the specified database
GRANT SELECT, UPDATE, DELETE ON utumishi.*
    TO 'job'@'localhost';

GRANT ALL ON *.* 
    TO 'job'@'localhost' WITH GRANT OPTION;
-- WITH GRANT OPTION should be left out if the user need not to be able to grant other users

-- avoid using reserved keyword in column or table name, if must try use back-tick `` delimiters

SELECT * FROM information_schema.PROCESSLIST ORDER BY INFO DESC, TIME DESC;

--  this is a bit more detail on time-frames // it will show all active and sleeping queries in that that order then by how long
SELECT ID, USER, HOST, DB, COMMAND,
TIME as time_seconds,
ROUND(TIME / 60, 2) as time_minutes,
ROUND(TIME / 60 / 60, 2) as time_hours,
STATE, INFO
FROM information_schema.PROCESSLIST ORDER BY INFO DESC, TIME DESC;

-- CHAR(n) if the character set utf8mb4, it occupies exactly 4*n bytes regardless of whattext is in it