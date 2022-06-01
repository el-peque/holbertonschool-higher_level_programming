#!/usr/bin/python3
"""Class declaration"""


class Student():
    """Class Student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if type(attrs) == list and all(isinstance(x, str) for x in attrs):
            d = {}
            for key in attrs:
                if key in self.__dict__:
                    d[key] = self.__dict__.get(key)
            return d
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        self.__dict__.update(json)
