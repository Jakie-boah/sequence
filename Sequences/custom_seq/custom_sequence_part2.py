

class MyClass:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'My Class {self.name}'

    def __add__(self, other):
        return MyClass(self.name + other.name)

    def __iadd__(self, other):
        if isinstance(other, MyClass):
            self.name += other.name
        else:
            self.name += other

        return self

    def __mul__(self, n):
        return MyClass(self.name * n)

    def __imul__(self, n):
        self.name *= n
        return self

    def __rmul__(self, n):
        return self.__mul__(n)

    def __contains__(self, value):
        return value in self.name



