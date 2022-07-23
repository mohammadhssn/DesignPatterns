"""
    Strategy:
        The strategy design pattern allows us to create a class that can choose different algorithms at runtime
        and work with them.
"""
from abc import ABC, abstractmethod


class Context:
    def __init__(self, direction, sentence):
        self._direction = direction
        self.sentence = sentence

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, dir):
        self._direction = dir

    def sorted(self):
        self._direction.direct(self.sentence)


class Direction(ABC):
    @abstractmethod
    def direct(self, data):
        pass


class Right(Direction):

    def direct(self, data):
        print(data[::-1])


class Left(Direction):

    def direct(self, data):
        print(data)


context_1 = Context(Right(), 'Hello World...')
context_2 = Context(Left(), 'Hello World...')
context_1.sorted()  # ...dlroW olleH
context_2.sorted()  # Hello World...
