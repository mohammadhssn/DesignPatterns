"""
    Creational => (They focus on how to create an object from a class):
        Abstract Factory:
            In Python,
            the abstract factory design pattern allows us to create an object that can be created in many different ways

        Example:
            Car => Benz , Bmw => suv, coupe
                   Benz suv   => Gla, Glb
                   Bmw suv    => X1, X2

                   Benz coupe => Cla, Clb
                   Bmw coupe  => M1, M2
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

    @staticmethod
    def call_suv(model):
        return model

    @staticmethod
    def call_coupe(model):
        return model


class Bmw(Car):

    @staticmethod
    def call_suv(model):
        return model

    @staticmethod
    def call_coupe(model):
        return model


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


class Gla(Suv, Benz):

    def creating_suv(self):
        print('This is your suv gla benz...')


class Glb(Suv, Benz):

    def creating_suv(self):
        print('This is your suv glb benz...')


class Cla(Suv, Bmw):

    def creating_suv(self):
        print('This is your suv cla bmw...')


class Clb(Suv, Bmw):

    def creating_suv(self):
        print('This is your suv clb bmw...')


# ----------------------------------------------------------------------------------------------------------------------


class X1(Coupe, Benz):

    def creating_coupe(self):
        print('This is your coupe x1 benz...')


class X2(Coupe, Benz):

    def creating_coupe(self):
        print('This is your coupe x2 benz...')


class M1(Coupe, Bmw):

    def creating_coupe(self):
        print('This is your coupe m1 bmw...')


class M2(Coupe, Bmw):

    def creating_coupe(self):
        print('This is your coupe m2 bmw...')


# ----------------------------------------------------------------------------------------------------------------------

def order_suv(corp, model):  # corp is the company, model is the model of the car
    if issubclass(model, corp):  # check if the model is related to corp, so you cannot call M2 from Benz

        suv = corp().call_suv(model())
        suv.creating_suv()

    else:
        raise NameError()


def order_coupe(corp, model):  # corp is the company, model is the model of the car
    if issubclass(model, corp):  # check if the model is related to corp, so you cannot call M2 from Benz

        coupe = corp().call_coupe(model())
        coupe.creating_coupe()

    else:
        raise NameError()


# ----------------------------------------------------------------------------------------------------------------------


try:
    order_suv(Benz, Gla)
except (NameError,
        AttributeError):  # calling Corporation incorrectly will raise NameError, calling Model incorrectly will raise AttributeError
    print('Sorry, we dont have this model....')

try:
    order_coupe(Bmw, M2)
except (NameError, AttributeError):
    print('Sorry, we dont have this model....')
