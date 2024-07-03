class Squares:
    def __init__(self, length):
        self.length = length
        self.i = 0

    def __next__(self):
        print('__next__ called')

        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result

    def __iter__(self):
        print('__iter__ called')
        return self


aq = Squares(5)
sq_iterator = iter(aq)
for i in aq:
    print(i)

for i in aq:
    print(i)
