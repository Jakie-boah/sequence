def counter():
    i = 0

    def inc():
        nonlocal i
        i += 1
        return i

    return inc


cnt = counter()


# for _ in range(10):
#     print(cnt())


class CallableIterator:
    def __init__(self, callable_, sentinel):
        self.callable_ = callable_
        self.sentinel = sentinel
        self.is_consumed = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_consumed:
            raise StopIteration

        result = self.callable_()

        if result == self.sentinel:
            self.is_consumed = True
            raise StopIteration

        return result


cnt = counter()
cnt_iter = CallableIterator(cnt, 8)
for _ in range(10):
    print(next(cnt_iter))
