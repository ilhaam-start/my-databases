from lib.cohort import *

"""
cohort construct with id, name and starting_date
"""
def test_cohort_construct():
    cohort = Cohort(1, "Data Engineering", 04/2023)
    assert cohort.id == 1
    assert cohort.name == "Data Engineering"
    assert cohort.starting_date == 04/2023

# """
# Test the format as string
# """
# def test_format_as_string():
#     cohort = Cohort(1, "Data Engineering", 04/2023)
#     assert str(cohort) == "1 - Data Engineering - 04/2023"