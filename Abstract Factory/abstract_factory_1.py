"""
    Creational => (They focus on how to create an object from a class):
        Abstract Factory:
            In Python,
            the abstract factory design pattern allows us to create an object that can be created in many different ways


        Example:
            Car => Benz, Bmw => suv, coupe
                   Benz suv     => Gla
                   Benz coupe   => X1

                   Bmw suv     => Cla
                   Bmw coupe   => M1
"""

from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def call_suv(self):
        pass

    @abstractmethod
    def call_coupe(self):
        pass


# ----------------------------------------------------------------------------------------------------------------------

class Benz(Car):

    def call_suv(self):
        return Gla()

    def call_coupe(self):
        return X1()


class Bmw(Car):

    def call_suv(self):
        return Cla()

    def call_coupe(self):
        return M1()


# ----------------------------------------------------------------------------------------------------------------------

class Suv(ABC):

    @abstractmethod
    def creating_suv(self):
        pass


class Coupe(ABC):

    @abstractmethod
    def creating_coupe(self):
        pass


# ----------------------------------------------------------------------------------------------------------------------

class Gla(Suv):

    def creating_suv(self):
        print('This is your suv benz gla...')


class Cla(Suv):

    def creating_suv(self):
        print('This is your suv bmw cla...')


# ----------------------------------------------------------------------------------------------------------------------
class X1(Coupe):

    def creating_coupe(self):
        print('This is your coupe benz x1...')


class M1(Coupe):

    def creating_coupe(self):
        print('This is your coupe bmw m1...')


# ----------------------------------------------------------------------------------------------------------------------

def client_suv(order):
    product = order.call_suv()
    product.creating_suv()


def client_coupe(order):
    product = order.call_coupe()
    product.creating_coupe()


client_suv(Benz())
client_suv(Bmw())

client_coupe(Benz())
client_coupe(Bmw())
