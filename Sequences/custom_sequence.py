my_list = [1, 2, 3, 4, 5]


class Silly:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        print('called __len__')
        return self.n

    def __getitem__(self, value):
        print(type(value))
        print(f'you requested item at {value}')
        return 'this is silly element'


silly = Silly(10)
silly[0]

from functools import lru_cache


@lru_cache(2 ** 10)
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(100))


class Fib:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 0:
                s = self.n + s

            if s < 0 or s >= self.n:
                raise IndexError
            else:
                return Fib._fib(s)
        else:
            # s is a slice
            start, stop, step = s.indices(self.n)
            rng = range(start, stop, step)
            return [Fib._fib(i) for i in rng]

    @staticmethod
    @lru_cache(2 ** 10)
    def _fib(n):
        if n < 2:
            return 1
        else:
            return Fib._fib(n - 1) + Fib._fib(n - 2)


fib = Fib(10)
print(list(fib))

print(fib[-1:-4])
