class User:
    def __init__(self, id, email_addres, username):
        self.id = id
        self.email_address = email_addres
        self.username = username
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"User Details({self.id} - {self.email_address} - {self.username})"