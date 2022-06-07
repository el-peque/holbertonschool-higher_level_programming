#!/usr/bin/python3
""" Base """
import json
import csv


class Base():
    """class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class initializer"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        if list_objs is None:
            list = []
        else:
            list = [i.to_dictionary() for i in list_objs]
        with open(cls.__name__ + ".json", mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 2)
        if cls.__name__ == "Square":
            dummy = cls(2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        try:
            with open(cls.__name__ + ".json", mode="r", encoding="utf-8") as f:
                data = f.read()
            list = cls.from_json_string(data)
            return [cls.create(**i) for i in list]

        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes in CSV """
        if list_objs is None:
            list = []
        else:
            list = [i.to_dictionary() for i in list_objs]
        with open(cls.__name__ + ".csv", mode="w", encoding="utf-8") as f:
            for dic in list:
                writer = csv.writer(f)
                if cls.__name__ == "Rectangle":
                    f.write(f"{dic.get('id')},{dic.get('width')},\
{dic.get('height')},{dic.get('x')},{dic.get('y')}")
                if cls.__name__ == "Square":
                    f.write(f"{dic.get('id')},{dic.get('size')},{dic.get('x')},{dic.get('y')}")

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes in CSV """
        try:
            with open(cls.__name__ + ".json", mode="r", encoding="utf-8") as f:
                data = f.read()
            list = cls.from_json_string(data)
            return [cls.create(**i) for i in list]

        except IOError:
            return []
