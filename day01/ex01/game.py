#!/usr/bin/env python


class GotCharacter:
    def __init__(self, first_name, is_alive):
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    """A class representing the Stark family. \
Or when bad things happen to good people."""

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False


class Lannister(GotCharacter):
    """A class representing the Lannister family. \
Or when good things happen to bad people."""

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.house_words = "A Lannister always pays his debts"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False


def test_class(name, theFamily):
    print(f"Testing character {name} of house {theFamily}")
    char = theFamily(name)
    print(char.__dict__)
    char.print_house_words()
    print(char.is_alive)
    print(char.__doc__)


def unit_tests():
    test_class('Arya', Stark)
    test_class('Cersei', Lannister)


if __name__ == '__main__':
    unit_tests()
