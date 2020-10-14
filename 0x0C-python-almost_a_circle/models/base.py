#!/usr/bin/python3
"""Module for Base superclass."""
from os import path
import json
import csv
import turtle
import random


class Base:
    """This superclass will be the "base" of all other classes."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor - Manage id attribute in future classes."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This method returns the JSON string representation
        of a list of dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This method writes the JSON string representation
        of a list of instances(objects) to a file.
        """
        json_file = cls.__name__ + ".json"
        empty_list = []

        if list_objs is not None:
            for run in list_objs:
                empty_list.append(run.to_dictionary())

        with open(json_file, "w") as f:
            f.write(cls.to_json_string(empty_list))

    @staticmethod
    def from_json_string(json_string):
        """
        This method returns the JSON string to a list of
        dictionaries.
        """
        if json_string is None and not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        This method creates a "dummy" instance and updates the
        value of the attributes with those of the given dictionary
        and returns a new object with all attributes already set.
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            obj = Rectangle(26, 19)

        elif cls is Square:
            obj = Square(31)

        else:
            obj = None

        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """
        This method determine if the file exist and returns
        a list of instances(objects) with the id.
        """
        json_file = cls.__name__ + ".json"
        empty_list = []

        if path.isfile(json_file):
            with open(json_file, "r") as f:
                dictionary = cls.from_json_string(f.read())
            for element in dictionary:
                empty_list.append(cls.create(**element))
        return empty_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """This method save to CSV file."""
        csv_file = cls.__name__ + ".csv"

        for run in list_objs:
            _dict = run.to_dictionary()
        k = _dict.keys()

        with open(csv_file, "w", newline="") as f:
            writer = csv.DictWriter(f, k)
            writer.writeheader()
            for i in list_objs:
                writer.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """This method loads and reads a CSV file."""
        csv_file = cls.__name__ + ".csv"
        empty_list = []

        if path.isfile(csv_file):
            with open(csv_file, "r", newline="") as f:
                reader = csv.DictReader(f)
                for dictionary in reader:
                    for key, value in dictionary.items():
                        dictionary[key] = int(value)
                    empty_list.append(cls.create(**dictionary))
            return empty_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """This method draws all the Rectangles and Squares."""
        turtle.Screen()
        turtle.bgcolor("#000C23")
        sammy = turtle.Turtle()

        for walk in list_rectangles + list_squares:
            r = random.random()
            g = random.random()
            b = random.random()
            sammy.color(r, g, b)
            sammy.speed(1.5)
            sammy.pensize(1)
            sammy.begin_fill()
            sammy.goto(walk.x, walk.y)
            sammy.pendown()
            sammy.backward(walk.width)
            sammy.pensize(2)
            sammy.right(90)
            sammy.backward(walk.height)
            sammy.pensize(3)
            sammy.right(90)
            sammy.backward(walk.width)
            sammy.pensize(4)
            sammy.right(90)
            sammy.backward(walk.height)
            sammy.pensize(5)
            sammy.right(90)
            sammy.penup()
            sammy.end_fill()

        turtle.exitonclick()
