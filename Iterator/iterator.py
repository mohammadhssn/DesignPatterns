"""
    Iterator:
        The iterator design pattern allows us to create our own sequence and
         determine how that sequence should be traversed.


        1.iterable  => It is a class that we want to navigate
        2.iteration => It is a class that determines how to navigate

        __iter__ , __next__
"""


class Iteration:
    def __init__(self, value):
        self.value = value

    def __next__(self):
        if self.value == 0:
            raise StopIteration('End of Sequence...')
        for _ in range(0, self.value):
            value = self.value
            self.value -= 1
            return value


class Iterable:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return Iteration(self.value)


iterable_1 = Iterable(10)
iterable_2 = iter(iterable_1)

print(next(iterable_2))
print(next(iterable_2))
print(next(iterable_2))
print(next(iterable_2))
print(next(iterable_2))
print(next(iterable_2))
print(next(iterable_2))
print(next(iterable_2))
print(next(iterable_2))
print(next(iterable_2))
print(next(iterable_2))
