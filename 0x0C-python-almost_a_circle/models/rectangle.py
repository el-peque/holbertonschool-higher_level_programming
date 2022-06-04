#!/usr/bin/python3
""" rectangle """
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class initializer"""
        __width = width
        __height = height
        __x = x
        __y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ widtth setter """
        self.__width = width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ height setter """
        self.__height = height
