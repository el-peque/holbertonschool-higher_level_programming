#!/usr/bin/python3
"""Class declaration"""


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry"""

    def __innit__(self, width, height):
        """Instantiation with width and height"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        __width = width
        __height = height
