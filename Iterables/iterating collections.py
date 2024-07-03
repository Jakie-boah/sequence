import random

s = {'x', 'y', 'b'}
for i in s:
    print(i)


# s[0] # не работает


class Squares:
    def __init__(self):
        self.i = 0

    def next_(self):
        result = self.i ** 2
        self.i += 1
        return result


sq = Squares()
sq.next_()
sq.next_()
print(sq.next_())

sq = Squares()
for i in range(5):
    print(sq.next_())


class Squares:
    def __init__(self, length):
        self.i = 0
        self.length = length

    def __len__(self):
        return self.length

    def next_(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result


print('----------')
# sq = Squares(3)
# print(len(sq))
# sq.next_()
# sq.next_()
# sq.next_()
# sq.next_()
a = Squares(10)


# while True:
#     try:
#         print(a.next_())
#     except StopIteration:
#         break


class Squares:
    def __init__(self, length):
        self.i = 0
        self.length = length

    def __len__(self):
        return self.length

    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result


sq = Squares(10)
while True:
    try:
        print(next(sq))
    except StopIteration:
        break


class RandomNumbers:
    def __init__(self, length, *, range_min=0, range_max=10):
        self.length = length
        self.range_min = range_min
        self.range_max = range_max
        self.num_requested = 0

    def __len__(self):
        return self.length

    def __next__(self):
        if self.num_requested >= self.length:
            raise StopIteration
        else:
            self.num_requested += 1
            return random.randint(self.range_min, self.range_max)
