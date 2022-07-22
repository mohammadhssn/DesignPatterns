"""
    Structural: (There are design patterns that focus on how classes interact with each other)
        Adapter:
            The adapter design pattern allows us to connect classes that cannot work together
            by creating an interface class.

            1. Adaptee -> The product that is going to change
            2. Adapter -> The one who makes the change
            3. Client  -> A user who wants to change her product
"""


class IranSocket:
    _type = '2'


class Adapter:
    _socket = None
    _pin_type = '3To2'

    def __init__(self, socket):
        self._socket = socket


class Fridge:
    _adapter = None
    _type = '3'

    def __init__(self, adapter):
        self._adapter = adapter

    def freeze(self):
        if self._adapter._pin_type == (self._type + 'To' + self._adapter._socket._type):
            print('Done...')
        else:
            print('Sorry! Not Usable')


iran_socket = IranSocket()
adapter = Adapter(socket=iran_socket)

fridge = Fridge(adapter=adapter)
fridge.freeze()
