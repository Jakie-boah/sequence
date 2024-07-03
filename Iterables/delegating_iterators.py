from collections import namedtuple

Person = namedtuple('Person', 'first last')


class PersonNames:
    def __init__(self, persons):
        self._persons = [person.first.capitalize() + ' ' + person.last.capitalize() for person in persons]

    def __iter__(self):
        return iter(self._persons)


persons = [Person('John', 'Doe'), Person('Jane', 'Doe'), Person('Mary', 'Doe')]
person_names = PersonNames(persons)
for name in person_names:
    print(name)
