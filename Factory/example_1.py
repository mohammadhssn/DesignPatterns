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


class File:
    def __init__(self, name, format):
        self.name = name
        self.format = format


class EditFile:

    def edit(self, file):  # Client
        return self._get_edit(file)

    def _get_edit(self, file):  # Creator
        if file.format == 'json':  # format => Identifier
            return self.json_edit
        elif file.format == 'xml':
            return self.xml_edit
        else:
            raise ValueError('invalid format...')

    def json_edit(self, file):  # Product
        print(f'Editing Json File... {file.name}')

    def xml_edit(self, file):
        print(f'Editing Xml File... {file.name}')


file = File('file name', 'json')
edit_file = EditFile()
edit_file.edit(file)
