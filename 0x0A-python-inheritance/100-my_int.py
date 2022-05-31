#!/usr/bin/python3
"""Class declaration"""


class MyInt(int):
    """class MyInt that inherits from int"""

    def __init__(self, num):
        self.__num = num

    def __eq__(self, n):
        return super().__ne__(n)

    def __ne__(self, n):
        return super().__eq__(n)
