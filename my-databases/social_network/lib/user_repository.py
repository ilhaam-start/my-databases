from lib.user import User

class UserRepository:
    
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        users = self._connection.execute('SELECT * FROM user_accounts')
        all_users = []
        for user in users:
            item = User(user["id"], user["email_address"], user["username"])
            all_users.append(item)
        return all_users