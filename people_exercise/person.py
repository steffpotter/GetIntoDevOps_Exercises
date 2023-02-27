# define superclass called Parent
class Person:

    # constructor
    def __init__(self, firstname, lastname):
        self._firstname = firstname
        self._lastname = lastname

    # overload the str method for this object
    def __str__(self):
        return f"\nName: {self._firstname} {self._lastname}"
