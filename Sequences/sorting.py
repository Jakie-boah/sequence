t = 1, 2, 3, 4, 7, 8, 5, 6, 9, 10

print(sorted(t))

d = {3: 100, 2: 200, 1: 300}
print(sorted(d.values()))
print(sorted(d, key=lambda k: d[k]))


class MyClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f'MyClass(name={self.name}, value={self.value})'

    def __lt__(self, other):
        return self.value < other.value


c1 = MyClass('c1', 20)
c2 = MyClass('c2', 10)
c3 = MyClass('c3', 20)
c4 = MyClass('c4', 10)

print(c1 < c2)
print(sorted([c1, c2, c3, c4]))