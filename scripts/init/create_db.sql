-- drop tables
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS groups;

-- create tables
CREATE TABLE groups (
    number VARCHAR(6) PRIMARY KEY
);

CREATE TABLE student (
    name VARCHAR(128),
    groups VARCHAR(6) REFERENCES groups(number),
    PRIMARY KEY(name, groups)
);

-- grand rights
GRANT ALL ON DATABASE suai TO postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON ALL TABLES IN SCHEMA public TO postgres;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO postgres;

ALTER TABLE groups OWNER TO postgres;
ALTER TABLE student OWNER TO postgres;
