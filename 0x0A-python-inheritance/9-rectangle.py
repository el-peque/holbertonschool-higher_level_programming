#!/usr/bin/python3
"""Class declaration"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation with width and height"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns area"""
        return self.__height * self.__width

    def __str__(self):
        """Returns str"""
        return f"[Rectangle] {self.__width}/{self.__height}"
