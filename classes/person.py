from abc import ABC, abstractmethod

"""
step sub-classes must implement method process
"""


class Person(ABC):

    def __init__(self, firstname,surname, age):
        # if self.__class__ == Person:
        #     raise Exception("I am abstract!")
        self.firstname = firstname
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"Name: {self.firstname}, Surname: {self.surname} Age: {self.age}"

    def __eq__(self, other):
        return self.firstname == other.firstname and\
               self.age == other.age and\
               self.surname == other.surname

    def __ne__(self, other):
        return not self.__eq__(other)







