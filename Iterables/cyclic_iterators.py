class CyclicIterator:

    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.lst[self.i % len(self.lst)]
        self.i += 1
        return result


# iter_cycle = CyclicIterator('NSWE')
#
# for item in iter_cycle:
#     print(item)

iter_cycle = CyclicIterator([10, 20, 35])

for _ in range(10):
    print(next(iter_cycle))

numbers = range(10)
iter_cycle = CyclicIterator('NSWE')
list(zip(list(numbers), iter_cycle))

n = 10
iter_cycle = CyclicIterator('NSWE')
items = [f'{i}{next(iter_cycle)}' for i in range(1, n + 1)]
print(items)

n = 10
iter_cycle = CyclicIterator('NSWE')

items = [f'{point}{direction}' for point, direction in zip(range(1, n + 1), iter_cycle)]
print(items)


class CyclicIterator:

    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(self.iterable)

    def __iter__(self):
        print(self)
        return self

    def __next__(self):
        try:
            item = next(self.iterator)

        except StopIteration:
            self.iterator = iter(self.iterable)
            item = next(self.iterator)

        return item 


iter_cycle = CyclicIterator('abc')

for i in range(10):
    print(i, next(iter_cycle))
