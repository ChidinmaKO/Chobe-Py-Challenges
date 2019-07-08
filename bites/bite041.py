from functools import wraps

known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


# def login_required(func):
#     @wraps(func)
#     def wrapper(*args):
#         for user in args:
#             if not user in known_users:
#                 return f"please create an account"
#             if not user in loggedin_users:
#                 return f"please login"
#             if user in known_users and loggedin_users:
#                 return f"welcome back {user}"
#         return func(*args)
#     return wrapper

# better way
def login_required(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user in known_users:
                return f"please create an account"
        if not user in loggedin_users:
            return f"please login"
        
        return func(user, *args, **kwargs)
    return wrapper

@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    # return user
    return f"welcome back {user}"

# tests
# from login import welcome


def test_no_account():
    """User is not on the system"""
    assert welcome('anonymous') == 'please create an account'


def test_not_loggedin():
    """User is on the system but not logged in"""
    assert welcome('julian') == 'please login'


def test_loggedin():
    """User is on the system and logged in"""
    assert welcome('sue') == 'welcome back sue'


def test_docstring():
    """Decorator should not lose function's docstring"""
    assert welcome.__doc__ == 'Return a welcome message if logged in'