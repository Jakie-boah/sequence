import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self._area = None

    @property
    def area(self):
        if self._area:
            print('площадь посчитана')
            return self._area
        else:
            print('считаю площадь')
            self._area = math.pi * self._radius ** 2
            return self._area


c = Circle(1)
print(c.area)
c.radius = 2
print(c.area)
print(c.area)
c.radius = 3
print(c.area)
print(c.area)


class Factorials:

    def __iter__(self):
        return self.FactIter()

    class FactIter:
        def __init__(self):
            self.i = 1

        def __iter__(self):
            return self

        def __next__(self):
            result = math.factorial(self.i)
            self.i += 1
            return result


facts = Factorials()
fact_iter = iter(facts)
print(next(fact_iter))
print(next(fact_iter))
print(next(fact_iter))
print(next(fact_iter))

d = zip(range(5), range(5))
for i in d:
    print(i)
print(len(list(d)))
for i in d:
    print(i)
