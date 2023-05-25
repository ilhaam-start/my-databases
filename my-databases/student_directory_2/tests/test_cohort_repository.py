from lib.cohort_repository import *
from lib.cohort import *
from tests.test_database_connection import *


"""
when #all is called, this gets all the cohorts back in a list
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repo = CohortRepository(db_connection)
    cohorts = repo.all()
    assert [str(cohort) for cohort in cohorts] == [
        "1 - Data Engineering - 04/2023",
        "2 - Software Engineering - 05/2023",
        "3 - Quality Engineering - 04/2023",
        "4 - DevOps - 02/2023"
    ]

"""
when #find is called, the item is returned.
"""
def test_find_get_item(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repo = CohortRepository(db_connection)
    cohorts = repo.find(1)
    assert str(cohorts) == "1 - Data Engineering - 04/2023"

"""
when #find_with_students is called, the cohort item is returned.
"""
def test_find_with_student_get_item(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repo = CohortRepository(db_connection)
    cohort = repo.find_with_students(1)
    assert str(cohort) == "1 - Student1 - 04/2023", "1 - Data Engineering - 04/2023"