"""
    Behavioral => (They focus on how classes and objects are supposed to work with each other)

        Template Method:
            The state pattern is a behavioral software design pattern that allows an object to change its behavior
            when its internal state changes.
            This can be a cleaner way for an object to change its behavior at runtime
            without using conditional statements, thereby improving code quality.
"""

from abc import ABC, abstractmethod


class Top(ABC):

    def template_method(self):
        self.first_common()
        self.two_common()
        self.third_require()
        self.fourth_require()
        self.hook()

    def first_common(self):
        print('i am first common...')

    def two_common(self):
        print('i am two common...')

    @abstractmethod
    def third_require(self):
        pass

    @abstractmethod
    def fourth_require(self):
        pass

    def hook(self):
        pass


class One(Top):

    def third_require(self):
        print('I am third require from one...')

    def fourth_require(self):
        print('I am fourth require from one...')

    def hook(self):
        print('I am hook form one...')


class Two(Top):

    def third_require(self):
        print('I am third require from two...')

    def fourth_require(self):
        print('I am fourth require from two...')


def client(klass):
    klass.template_method()


client(One())
print('**************')
client(Two())
