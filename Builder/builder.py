"""
    Creational => (They focus on how to create an object from a class):
        Builder:
            The design pattern builder is used when we are going to make a product that is made of smaller components,
            and those smaller components must be created so that we can use them.
"""
from abc import ABC, abstractmethod


class Director:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_car(self):
        car = Car()

        body = self.__builder.get_body()
        car.set_body(body)

        wheel = self.__builder.get_wheel()
        car.set_wheel(wheel)

        engine = self.__builder.get_engine()
        car.set_engine(engine)

        return car


# ----------------------------------------------------------------------------------------------------------------------
class Car:
    def __init__(self):
        self.__body = None
        self.__wheel = None
        self.__engine = None

    def set_body(self, body):
        self.__body = body

    def set_wheel(self, wheel):
        self.__wheel = wheel

    def set_engine(self, engine):
        self.__engine = engine

    def detail(self):
        print(f'Body: {self.__body.shape}')
        print(f'Wheel: {self.__wheel.size}')
        print(f'Engine: {self.__engine.hp}')


# ----------------------------------------------------------------------------------------------------------------------
class Builder(ABC):

    @abstractmethod
    def get_body(self):
        pass

    @abstractmethod
    def get_wheel(self):
        pass

    @abstractmethod
    def get_engine(self):
        pass


class Benz(Builder):

    def get_body(self):
        body = Body()
        body.shape = 'Suv'
        return body

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def get_engine(self):
        engine = Engine()
        engine.hp = 450
        return engine


class Bmw(Builder):

    def get_body(self):
        body = Body()
        body.shape = 'Sedan'
        return body

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 18
        return wheel

    def get_engine(self):
        engine = Engine()
        engine.hp = 800
        return engine


# ----------------------------------------------------------------------------------------------------------------------
class Body:
    shape = None


class Wheel:
    size = None


class Engine:
    hp = None


# ----------------------------------------------------------------------------------------------------------------------


bmw = Bmw()
director = Director()
director.set_builder(bmw)

car = director.get_car()
car.detail()
