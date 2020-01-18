# see __mro__ output in Bite description# see __mro__ output in Bite description


class Person:
    def __str__(self):
        return f"I am a person"

class Father(Person):
    def __str__(self):
        return f"{super().__str__()} and cool daddy" 

class Mother(Person):
    def __str__(self):
        return f"{super().__str__()} and awesome mom"

class Child(Father, Mother):
    def __str__(self):
        return f"I am the coolest kid"


# tests

import inspect

import pytest

from person import Person, Father, Mother, Child


@pytest.fixture
def person():
    return Person()


@pytest.fixture
def dad():
    return Father()


@pytest.fixture
def mom():
    return Mother()


@pytest.fixture
def child():
    return Child()


def test_string_repr_person(person):
    assert str(person) == 'I am a person'


def test_string_repr_dad(dad):
    assert str(dad) == 'I am a person and cool daddy'


def test_string_repr_mom(mom):
    assert str(mom) == 'I am a person and awesome mom'


def test_string_repr_child(child):
    assert str(child) == 'I am the coolest kid'


def test_mro_of_person():
    assert Person.__mro__ == (Person, object)


def test_mro_of_dad():
    assert Father.__mro__ == (Father, Person, object)


def test_mro_of_mom():
    assert Mother.__mro__ == (Mother, Person, object)


def test_mro_of_child():
    assert Child.__mro__ == (Child, Father, Mother, Person, object)


def test_subclass_person():
    assert issubclass(Person, object)


def test_subclass_dad():
    assert issubclass(Father, Person)
    assert issubclass(Father, object)


def test_subclass_mom():
    assert issubclass(Mother, Person)
    assert issubclass(Mother, object)


def test_subclass_child():
    assert issubclass(Child, Father)
    assert issubclass(Child, Mother)
    assert issubclass(Child, Person)
    assert issubclass(Child, object)


def test_use_inheritance():
    # dry code!
    # should not duplicate substr in subclass
    substr = 'I am a person'
    for src in (inspect.getsource(Father),
                inspect.getsource(Mother)):
        assert substr not in src