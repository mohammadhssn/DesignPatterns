"""
    Behavioral => (They focus on how classes and objects are supposed to work with each other

        Observer:
            In this video, you will learn about the observer design pattern.
            The observer pattern is a software design pattern in which an object named subject keeps
            a list of its dependents called observers, and usually by calling one of its methods,
            it automatically protects them from any state changes.
            informs The Observer pattern is used when there is one or more relationships between objects,
            such as when an object is modified, its dependent objects are automatically notified.
            The Observer pattern is placed in the behavioral pattern classification.

        sample:
            In Django and Flask, the observer design pattern is used in the signals section
"""


class Observer:

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)


class Person(Observer):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
        self.notify()


class One:
    def update(self, subject):
        print(f'One: {subject.name} new {subject.age}')


class Two:
    def update(self, subject):
        print(f'Two: {subject.name} new {subject.age}')


person = Person('mohammadhssn')
one = One()
two = Two()

person.attach(one)
person.attach(two)

person.age = 23
