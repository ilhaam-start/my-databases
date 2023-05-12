CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  starting_date int
);

-- Then the table with the foreign key second.
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort_id int,
  constraint fk_cohort_id foreign key(cohort_id) references cohorts(id) on delete cascade
);
