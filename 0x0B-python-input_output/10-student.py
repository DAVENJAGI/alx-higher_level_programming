#!/usr/bin/python3
"""Creates a class"""


class Student:
    """Reps a student"""
    def __init__(self, first_name, last_name, age):
        """initializes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """Dictionary rep of students"""
        if type(attr) == list and all(type(ele) == str for ele in attr):
            return {k: getattr(self, k) for k in attr if hasattr(self, k)}
        return (self.__dict__)
