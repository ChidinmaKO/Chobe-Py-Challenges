from functools import wraps

UPPER_SLICE = "=== Upper bread slice ==="
LOWE_SLICE = "=== Lower bread slice ==="


def sandwich(func):
    """Write a decorator that prints UPPER_SLICE and
       LOWE_SLICE before and after calling the function (func)
       that is passed in  (@wraps is to preserve the original
       func's docstring)
    """
    @wraps(func)
    def wrapped(*args, **kwargs):
        print(UPPER_SLICE)
        func(*args, **kwargs)
        print(LOWE_SLICE)
    return wrapped

# tests
# from sandwich import sandwich

SANDWICH_BACON = """=== Upper bread slice ===
bacon / lettuce / tomato
=== Lower bread slice ===
"""
SANDWICH_EGG = """=== Upper bread slice ===
fried egg / tomato / cucumber
=== Lower bread slice ===
"""


@sandwich
def add_ingredients(ingredients):
    print(' / '.join(ingredients))


def test_bacon_sandwich(capfd):
    ingredients = ['bacon', 'lettuce', 'tomato']
    add_ingredients(ingredients)
    actual = capfd.readouterr()[0]
    assert actual == SANDWICH_BACON


def test_fried_egg_sandwich(capfd):
    ingredients = ['fried egg', 'tomato', 'cucumber']
    add_ingredients(ingredients)
    actual = capfd.readouterr()[0]
    assert actual == SANDWICH_EGG