# -*- coding: utf-8 -*- 

from character import Character



class Card(object):
        def __init__(self, name, point, char_name):
                self.name = name
                self.point = point
                self.char_name = char_name
                self.char = None

        def __eq__(self, other):
                if isinstance(other, Character):
                        return self.char_name == other.name
                else:
                        return self.name == other.name

        def __ne__(self, other):
                return self.name != other.name

        def __ge__(self, other):
                return self.point >= other.point

        def __gt__(self, other):
                return self.point > other.point

        def __le__(self, other):
                return self.point <= other.point

        def __lt__(self, other):
                return self.point < other.point

        def __add__(self, other):
                return self.point + other.point

        def __radd__(self, num):
                return self.point + num

        def __repr__(self):
                return self.char_name + ': ' + self.name

        def __str__(self):
                return self.char_name + ': ' + self.name

        def add_char(self, char):
                if char.name == self.char_name:
                        self.char = char
