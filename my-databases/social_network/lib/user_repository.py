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
    
    def find(self, id):
        users = self._connection.execute(
            'SELECT * from user_accounts WHERE id = %s', [id])
        user = users[0]
        return User(user["id"], user["email_address"], user["username"])
    
    def create(self, account):
        self._connection.execute('INSERT INTO user_accounts (id, email_address, username) VALUES (%s, %s, %s)', [
                                account.id, account.email_address, account.username])
        return None
    
    def update(self, user_id, new_email, new_username):
        self._connection.execute('UPDATE user_Accounts SET email_address = %s, username = %s WHERE id = %s', [new_email, new_username, user_id])
        return None

    def delete(self, id):
        self._connection.execute(
            'DELETE FROM user_accounts WHERE id = %s', [id])
        return None