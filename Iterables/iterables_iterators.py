class Cities:
    def __init__(self):
        self._cities = ['Paris', 'London', 'Berlin', 'Madrid', 'Rome', ]
        self._index = 0

    def __iter__(self):
        # self._index = 0
        return self

    def __next__(self):
        if self._index >= len(self._cities):
            raise StopIteration
        else:
            item = self._cities[self._index]
            self._index += 1
            return item


cities = Cities()
print(list(enumerate(cities)))
print(list(enumerate(cities)))
