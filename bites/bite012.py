from collections import namedtuple

User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=False)
bob = User(name='Bob', role=USER, expired=True)
pybites = User(name='PyBites', role=ADMIN, expired=False)
USERS = (julian, bob, pybites)

# define exception classes here
class UserDoesNotExist(Exception):
    pass

class UserAccessExpired(Exception):
    pass

class UserNoPermission(Exception):
    pass

def get_secret_token(username):
    all_users = {user.name: user for user in USERS}
    
    user = all_users.get(username)
    
    if user not in USERS:
        raise UserDoesNotExist
    elif user.expired:
        raise UserAccessExpired
    elif not user.role == ADMIN:
        raise UserNoPermission
    else:
        return SECRET
    
    
# tests
import pytest

# from validate import (get_secret_token, SECRET, UserDoesNotExist, UserAccessExpired, UserNoPermission)


def test_get_secret_token():
    assert issubclass(UserDoesNotExist, Exception)
    assert issubclass(UserAccessExpired, Exception)
    assert issubclass(UserNoPermission, Exception)

    with pytest.raises(UserDoesNotExist):
        get_secret_token('Tim')
    with pytest.raises(UserAccessExpired):
        get_secret_token('Bob')
    with pytest.raises(UserNoPermission):
        get_secret_token('Julian')

    assert get_secret_token('PyBites') == SECRET