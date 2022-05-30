#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Class declaration"""


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation with width and height"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
