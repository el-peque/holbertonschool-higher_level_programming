#!/usr/bin/python3
class LockedClass:
    """no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name"""
    __slots__= ['name']
    def __init__(self, name=""):
        """first name"""
        self.first_name = name
