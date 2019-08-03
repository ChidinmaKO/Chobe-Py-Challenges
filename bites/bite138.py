from itertools import count

class Animal:
    count_ = count(10001, 1)
    _zoo = []

    def __init__(self, name):
        self.name = name.title()
        self.num = next(self.count_)
        self.animal = f"{self.num}. {self.name}"
        self._zoo.append(self.animal)

    def __str__(self):
        return self.animal

    @classmethod
    def zoo(cls):
        return cls._zoo


# tests

# from zoo import Animal


def test_zoo_5_animals():
    for animal in 'dog cat fish lion mouse'.split():
        Animal(animal)
    zoo = Animal.zoo()
    assert "10001. Dog" in zoo
    assert "10002. Cat" in zoo
    assert "10003. Fish" in zoo
    assert "10004. Lion" in zoo
    assert "10005. Mouse" in zoo


def test_animal_instance_str():
    horse = Animal('horse')
    assert str(horse) == "10006. Horse"
    horse = Animal('monkey')
    assert str(horse) == "10007. Monkey"