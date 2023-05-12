from lib.user_repository import UserRepository
from lib.user import User

"""
Test #all method
"""
def test_all_return_list(db_connection):
    db_connection.seed("seeds/social_network.sql")
    user_repo = UserRepository(db_connection)
    result = user_repo.all()
    assert result == [
        "User Details(1 - ilhaam777@gmail.com - ilhaam777)",
        "User Details(2 - ilhaam.ahmed@hotmail.com - ilhaam1)"
        "User Details(3 - ahmed@gmail.com - illy)"
        "User Details(4 - il.ah@gmail.com - ilham)"
    ]

"""
Test #find method
"""
def test_find_return_item(db_connection):
    db_connection.seed("seeds/social_network.sql")
    user_repo = UserRepository(db_connection)

"""
Test #create method
"""
def test_create_add_to_list(db_connection):
    db_connection.seed("seeds/social_network.sql")
    user_repo = UserRepository(db_connection)

"""
Test #update method
"""
def test_update_return_updated_list(db_connection):
    db_connection.seed("seeds/social_network.sql")
    user_repo = UserRepository(db_connection)

"""
Test #delete method
"""
def test_delete_return_shortened_list(db_connection):
    db_connection.seed("seeds/social_network.sql")
    user_repo = UserRepository(db_connection)