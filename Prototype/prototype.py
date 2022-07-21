"""
    Creational => (They focus on how to create an object from a class):
        Prototype:
            The prototype design pattern helps us to get a copy of an object that has already been created
            so that there is no need to create a new object, which saves resources.
"""
from copy import deepcopy


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Prototype:

    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        del self._objects[name]

    def clone(self, name, **kwargs):
        cloned_obj = deepcopy(self._objects.get(name))
        cloned_obj.__dict__.update(kwargs)
        return cloned_obj


person1 = Person('mohammadhssn', 23)

prototype1 = Prototype()
prototype1.register(name='person1', obj=person1)

person_copy1 = prototype1.clone('person1')
person_copy2 = prototype1.clone('person1', age=30)

print(person_copy1.__dict__)
print(person1.name is person_copy1.name)
print(person1.age is person_copy1.age)

print(person_copy2.__dict__)
