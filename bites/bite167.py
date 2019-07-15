class User:
    """A User class
       (Django's User model inspired us)
    """

    def __init__(self, first_name, last_name):
        """Constructor, base values"""
        self.first_name = first_name
        self.last_name = last_name

    @property
    def get_full_name(self):
        """Return first separated by a whitespace
           and using title case for both.
        """
        fullname = f"{self.first_name} {self.last_name}"
        return fullname.title()

    @property
    def username(self):
        """A username consists of the first char of
           the user's first_name and the first 7 chars
           of the user's lowercased last_name.

           If this is your first property, check out:
           https://pybit.es/property-decorator.html
        """
        username_ = f"{self.first_name[0]}{self.last_name[:7]}"
        return username_.lower()

    # see: https://stackoverflow.com/a/1438297
    # "__repr__ is for devs, __str__ is for customers"

    def __str__(self):
        return f"{self.get_full_name} ({self.username})"

    def __repr__(self):
        """Don't hardcode the class name, hint: use a
           special attribute of self.__class__ ...
        """
        return f'{self.__class__.__name__}("{self.first_name}", "{self.last_name}")'

# tests
# from user import User


def test_bob_lowercase():
    bob = User('bob', 'belderbos')
    assert bob.get_full_name == 'Bob Belderbos'
    assert bob.username == 'bbelderb'  # lowercase!
    assert str(bob) == 'Bob Belderbos (bbelderb)'
    assert repr(bob) == 'User("bob", "belderbos")'


def test_julian_mixed_case():
    bob = User('julian', 'Sequeira')
    assert bob.get_full_name == 'Julian Sequeira'
    assert bob.username == 'jsequeir'  # lowercase!
    assert str(bob) == 'Julian Sequeira (jsequeir)'
    assert repr(bob) == 'User("julian", "Sequeira")'


def test_tania_title_name():
    bob = User('Tania', 'Courageous')
    assert bob.get_full_name == 'Tania Courageous'  # aka PyBites Ninja
    assert bob.username == 'tcourage'  # lowercase!
    assert str(bob) == 'Tania Courageous (tcourage)'
    assert repr(bob) == 'User("Tania", "Courageous")'


def test_noah_use_dunder_in_repr():
    """Make sure repr does not have the class
       name hardcoded.
       Also tests for a shorter surname.
    """
    class SpecialUser(User):
        pass

    noah = SpecialUser('Noah', 'Kagan')
    assert noah.get_full_name == 'Noah Kagan'
    assert noah.username == 'nkagan'  # lowercase!
    assert str(noah) == 'Noah Kagan (nkagan)'

    # it should show the subclass!
    assert repr(noah) == 'SpecialUser("Noah", "Kagan")'