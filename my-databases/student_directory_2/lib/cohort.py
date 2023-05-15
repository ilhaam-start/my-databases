class Cohort:
    def __init__(self, id, name, starting_date):
        self.id = id
        self.name = name
        self.starting_date = starting_date

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"{self.id} - {self.name} - {self.starting_date}"