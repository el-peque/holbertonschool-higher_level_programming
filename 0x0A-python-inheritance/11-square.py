#!/usr/bin/python3
"""Class declaration"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square that inherits from Rectangle"""

    def __init__(self, size):
        """Instantiation with size"""
        super().integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """Returns area"""
        return self.__size ** 2

    def __str__(self):
        """Returns description"""
        return f"[Square] {self.__size}/{self.__size}"
