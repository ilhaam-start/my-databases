
DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS students_id_seq;

DROP TABLE IF EXISTS cohorts;
DROP SEQUENCE IF EXISTS cohorts_id_seq;


CREATE SEQUENCE IF NOT EXISTS cohorts_id_seq;
CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  starting_date text
);

CREATE SEQUENCE IF NOT EXISTS students_id_seq;
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort_id int,
  constraint fk_cohort_id foreign key(cohort_id)
      references cohorts(id)
      on delete cascade
);

INSERT INTO cohorts (name, starting_date) VALUES ('Data Engineering', '04/2023');
INSERT INTO cohorts (name, starting_date) VALUES ('Software Engineering', '05/2023');
INSERT INTO cohorts (name, starting_date) VALUES ('Quality Engineering', '04/2023');
INSERT INTO cohorts (name, starting_date) VALUES ('DevOps', '02/2023');

INSERT INTO students (name, cohort_id) VALUES ('Student1', 1);
INSERT INTO students (name, cohort_id) VALUES ('Student2', 1);
INSERT INTO students (name, cohort_id) VALUES ('Student3', 2);
INSERT INTO students (name, cohort_id) VALUES ('Student4', 3);
INSERT INTO students (name, cohort_id) VALUES ('Student5', 3);
INSERT INTO students (name, cohort_id) VALUES ('Student6', 4);
INSERT INTO students (name, cohort_id) VALUES ('Student7', 2);
INSERT INTO students (name, cohort_id) VALUES ('Student8', 1);