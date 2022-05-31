#!/usr/bin/python3
"""declaration"""


class Square:
    """square"""

    def __init__(self, size=0):
        """size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")

        self.__size = size

    def area(self):
        """area is equal to size**2"""
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for n in range(self.__size):
                    print("#", end="")
                print()
    @property
    def size(self):
        """returns size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size to value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value
