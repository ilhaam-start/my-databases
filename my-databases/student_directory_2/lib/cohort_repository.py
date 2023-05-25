from lib.cohort import *
from lib.student import *

class CohortRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM cohorts')
        cohorts = []
        for row in rows:
            item = Cohort(row["id"], row["name"], row["starting_date"])
            cohorts.append(item)
        return cohorts
    
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM cohorts WHERE id = %s', [id])
        row = rows[0]
        item = Cohort(row["id"], row["name"], row["starting_date"])
        return item
    
    def find_with_students(self, id):
        rows = self._connection.execute(
            "SELECT cohorts.id as cohort_id, cohorts.name, cohorts.starting_date, students.id AS student_id, students.name " \
            "FROM cohorts JOIN students ON cohorts.id = students.cohort_id " \
            "WHERE cohorts.id = %s", [id]
            )
        students =[]
        for row in rows:
            student = Student(row["student_id"], row["name"], row["cohort_id"])
            students.append(student)
        return Cohort(rows[0]["cohort_id"], rows[0]["name"], rows[0]["starting_date"], students=students)

    
    # def create(self, title, author_name):
    #     self._connection.execute('INSERT INTO books (title, author_name) VALUES (%s, %s)', [title, author_name])
    #     return None
    
    # def update(self, book_id, new_title, _new_author):
    #     self._connection.execute('UPDATE books SET title = %s, author_name = %s WHERE id = %s', [new_title, _new_author, book_id])
    #     return None
    
    # def delete(self, book_id):
    #     self._connection.execute('DELETE FROM books WHERE id = %s', [book_id])
    #     return None
