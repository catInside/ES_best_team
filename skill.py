# -*- coding: utf-8 -*- 

from character import Character



class Skill(object):
        def __init__(self, name, member_names, up):
                self.name = name
                self.member_names = set(member_names)
                self.members = set()
                self.up = up

        def __contains__(self, other):
                if isinstance(other, Skill):
                        return other.member_names.issubset(self.member_names)
                elif isinstance(other, Character):
                        return other in self.members
                elif(other, str):
                        return other in self.member_names

        def __add__(self, other):
                return self.up + other.up

        def __radd__(self, num):
                return self.up + num

        def add_char(self, char):
                if char.name in self.member_names:
                        self.members.add(char)