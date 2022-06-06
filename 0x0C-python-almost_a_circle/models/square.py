#!/usr/bin/python3
""" Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Intitializer """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, size):
        """ size setter """
        self.width = size
        self.height = size

    def __str__(self):
        """  returns '[Square] (<id>) <x>/<y> - <size>' """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        if args and len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]

        else:
            if 'id' in kwargs:
                self.id = kwargs.get('id')
            if 'size' in kwargs:
                self.width = kwargs.get('size')
            if 'x' in kwargs:
                self.x = kwargs.get('x')
            if 'y' in kwargs:
                self.y = kwargs.get('y')

    def to_dictionary(self):
        """ returns the dictionary representation of a Square """
        return dict(id=self.id, size=self.size, x=self.x, y=self.y)
