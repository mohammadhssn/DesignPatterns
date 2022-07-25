"""
    Structural: (There are design patterns that focus on how classes interact with each other)
        Composite:
            Composite is a structural design pattern that allows you to combine objects into tree structures
            and then work with these structures as if they were separate objects.
            Using the Composite pattern only makes sense when the main model of your application can be represented as a tree.
"""

from abc import ABC, abstractmethod


class World(ABC):

    @abstractmethod
    def show(self):
        pass


class Being(World):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, object):
        self.children.append(object)

    def remove(self, object):
        self.children.remove(object)

    def show(self):
        print(f'Being Composite {self.name}')
        for child in self.children:
            child.show()


# ---------------------------------------------------------------------------------------------------------------------

class Animal(World):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, object):
        self.children.append(object)

    def remove(self, object):
        self.children.remove(object)

    def show(self):
        print(f'\tAnimal Composite {self.name}')
        for child in self.children:
            child.show()


class Human(World):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, object):
        self.children.append(object)

    def remove(self, object):
        self.children.remove(object)

    def show(self):
        print(f'\tHuman Composite {self.name}')
        for child in self.children:
            child.show()


# ---------------------------------------------------------------------------------------------------------------------

class Cat(World):
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'\t\tCat Leaf {self.name}')


class Dog(World):
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'\t\tDog Leaf {self.name}')


# ---------------------------------------------------------------------------------------------------------------------

class Male(World):
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'\t\tMale Leaf {self.name}')


class Female(World):
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'\t\tFemale Leaf {self.name}')


# ---------------------------------------------------------------------------------------------------------------------


cat = Cat('cat')
dog = Dog('dog')

animal = Animal('animal')

animal.add(cat)
animal.add(dog)
# -----------------------
male = Male('male')
female = Female('female')

human = Human('human')

human.add(male)
human.add(female)
# -----------------------

being = Being('beibg')

being.add(animal)
being.add(human)

being.show()
