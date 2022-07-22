"""
    Structural: (There are design patterns that focus on how classes interact with each other)
        Facade:
            The facade design pattern allows us to hide the complexity of the program by an interface class
            and users only work with that interface class.
"""


class Raw:
    def raw(self):
        print('Buying raw foods from market...')


class Transfer:
    def transfer(self):
        print('Transfering raw foods to restaurant...')


class Cook:
    def cook(self):
        print('Cooking raw food by chief...')


class Serve:
    def serve(self):
        print('Serving food to client...')


class ItalianRestaurant:  # facade

    def get(self):
        raw = Raw()
        raw.raw()

        transfer = Transfer()
        transfer.transfer()

        cook = Cook()
        cook.cook()

        serve = Serve()
        serve.serve()


def order():
    i = ItalianRestaurant()
    i.get()


order()
