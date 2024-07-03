l = [1, 2, 3, 4]

l_iter = iter(l)
print(type(l_iter))

next(l_iter)
print(next(l_iter))


class Squares:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, i):
        if i >= self.n:
            raise IndexError

        return i ** 2


sq = Squares(10)
sq_iter = iter(sq)
print(type(sq_iter))

print('__next__' in dir(sq))


class SequenceIterator:
    def __init__(self, sequence):
        self._squares = sequence
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._i >= len(self._squares):
            raise StopIteration

        result = self._squares[self._i]
        self._i += 1
        return result


class SimpleIter:
    def __init__(self):
        pass

    def __iter__(self):
        return 'Nope'


s = SimpleIter()
print('__iter__' in dir(s))


def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False


print(is_iterable(s))
print(is_iterable(sq))

obj = 100
if is_iterable(obj):
    for i in obj:
        print(i)
else:
    print('obj not iterable')
