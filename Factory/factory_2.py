"""
    Creational => (They focus on how to create an object from a class):
        Factory:
            The factory design pattern allows us to create a superclass that is responsible for creating objects
            and allow subclasses to change the type of object that is created.

            3 component => 1.Creator 2.Product 3.Client
                1.Creator => (A part of the code that decides what type of object to create)
                2.Product => (A part of the code that produces something for us)
                3.Client => (The part of the code that the user deals with)
                Identifier => (Creator decides what object to make using it)

        example: The Factory design pattern is used in the Django Forms section
"""

from abc import ABC, abstractmethod


class Creator(ABC):
    """
        Base Class For Child
    """

    @abstractmethod
    def make(self):
        pass

    def call_edit(self):
        product = self.make()
        return product.edit()


class JsonCreator(Creator):

    def make(self):
        return JsonProduct()


class XmlCreator(Creator):

    def make(self):
        return XmlProduct()


class PdfCreator(Creator):

    def make(self):
        return PdfProduct()


# ----------------------------------------------------------------------------------------------------------------------
class Product(ABC):
    """
        Base Class For Child
    """

    @abstractmethod
    def edit(self):
        pass


class JsonProduct(Product):

    def edit(self):
        return 'Editing Json File...'


class XmlProduct(Product):

    def edit(self):
        return 'Editing Xml File...'


class PdfProduct(Product):

    def edit(self):
        return f'Editing Pdf File...'


# ----------------------------------------------------------------------------------------------------------------------
def client(format):
    return format.call_edit()


print(client(JsonCreator()))
print(client(XmlCreator()))
print(client(PdfCreator()))
