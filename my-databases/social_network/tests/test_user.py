from lib.user import User

"""
User constructs an email_address and username
"""
def test_construct_email_username():
    user = User(1,"ilhaam777@gmail.com", "ilhaam777")
    assert user.id == 1
    assert user.email_address == "ilhaam777@gmail.com"
    assert user.username == "ilhaam777"
