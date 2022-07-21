"""
    Creational => (They focus on how to create an object from a class):
        Singleton:
            Only one object can be created from a class
            example: In Python, 'imports' use singleton
"""


class Singleton(type):
    """
        Meta Class
    """

    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class Db(metaclass=Singleton):
    pass


db1 = Db()
db2 = Db()
db3 = Db()

print(id(db1))
print(id(db2))
print(id(db3))

print(db1 is db2 and db2 is db3)  # True
