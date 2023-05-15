from lib.user_repository import UserRepository
from lib.user import User

"""
Test #all method
"""
def test_all_return_list(db_connection):
    db_connection.seed("seeds/social_network.sql")
    user_repo = UserRepository(db_connection)
    result = user_repo.all()
    assert [str(result) for result in result] == [
        "User Details(1 - ilhaam777@gmail.com - ilhaam777)",
        "User Details(2 - ilhaam.ahmed@hotmail.com - ilhaam1)",
        "User Details(3 - ahmed@gmail.com - illy)",
        "User Details(4 - il.ah@gmail.com - ilham)"
    ]

"""
Test #find method
"""
def test_find_return_item(db_connection):
    db_connection.seed("seeds/social_network.sql")
    user_repo = UserRepository(db_connection)
    result = user_repo.find(3)
    assert str(result) == "User Details(3 - ahmed@gmail.com - illy)"

"""
Test #create method
"""
def test_create_add_to_list(db_connection):
    db_connection.seed("seeds/social_network.sql")
    user_repo = UserRepository(db_connection)
    user_repo.create(User(5, "hafsa.ahmed", "haffy"))
    result = user_repo.all()
    assert [str(result) for result in result] == [
        "User Details(1 - ilhaam777@gmail.com - ilhaam777)",
        "User Details(2 - ilhaam.ahmed@hotmail.com - ilhaam1)",
        "User Details(3 - ahmed@gmail.com - illy)",
        "User Details(4 - il.ah@gmail.com - ilham)",
        "User Details(5 - hafsa.ahmed - haffy)"
    ]

"""
Test #update method
"""
def test_update_return_updated_list(db_connection):
    db_connection.seed("seeds/social_network.sql")
    user_repo = UserRepository(db_connection)
    user_repo.update(2, "lalalla@gmail.com", "lalla")
    result = user_repo.find(2)
    assert str(result) == "User Details(2 - lalalla@gmail.com - lalla)"

"""
Test #delete method
"""
def test_delete_return_shortened_list(db_connection):
    db_connection.seed("seeds/social_network.sql")
    user_repo = UserRepository(db_connection)
    user_repo.delete(4)
    result = user_repo.all()
    assert [str(result) for result in result] == [
        "User Details(1 - ilhaam777@gmail.com - ilhaam777)",
        "User Details(2 - ilhaam.ahmed@hotmail.com - ilhaam1)",
        "User Details(3 - ahmed@gmail.com - illy)"
    ]