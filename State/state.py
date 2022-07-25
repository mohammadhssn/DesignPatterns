"""
    Behavioral => (They focus on how classes and objects are supposed to work with each other)

        State:
        The state pattern is a behavioral software design pattern that allows an object
                to change its behavior when its internal state changes.
        This can be a cleaner way for an object to change its behavior at runtime without using conditional statements,
        thereby improving code quality.
"""


class State:
    def operate(self):
        print(f'Turning Tv {self.status}')


class TurnOn(State):
    def __init__(self, tv):
        self.tv = tv
        self.status = 'On'

    def change_state(self):
        print('Changing state to off...')
        self.tv.state = self.tv.off


class TurnOff(State):
    def __init__(self, tv):
        self.tv = tv
        self.status = 'Off'

    def change_state(self):
        print('Changing state to on...')
        self.tv.state = self.tv.on


class Tv:
    def __init__(self):
        self.on = TurnOn(self)
        self.off = TurnOff(self)
        self.state = self.on

    def press(self):
        self.state.operate()
        self.state.change_state()


tv = Tv()
tv.press()  # On
tv.press()  # Off
