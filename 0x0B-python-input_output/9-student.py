#!/usr/bin/python3
"""Creates a class Student"""


class Student:
    """Reps a student"""
    def __init__(self, first_name, last_name, age):
        """initializes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary"""
        return (self.__dict__)
