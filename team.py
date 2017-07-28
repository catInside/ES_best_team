# -*- coding: utf-8 -*- 

from character import Character



class Team(object):
        def __init__(self, leader):
                self.leader = leader
                if leader is None:
                        self.members = set()
                else:
                        self.members = set([leader,])
                self.skills = set()
                self.up = 1.0

        def __contains__(self, other):
                if isinstance(other, Team):
                        return other.memebers.issubset(self.memebers)
                elif isinstance(other, Character):
                        return other in self.members

        def __eq__(self, other):
                return self.leader == other.leader and self.members == other.members

        def __ne__(self, other):
                return self.leader != other.leader or self.members != other.members

        def __ge__(self, other):
                return self.up >= other.up

        def __gt__(self, other):
                return self.up > other.up

        def __le__(self, other):
                return self.up <= other.up

        def __lt__(self, other):
                return self.up < other.up

        def add_member(self, character):
                if character not in self.members and len(self.members) < 5:
                        self.members.add(character)

        def add_skill_members(self, skill):
                if self.leader in skill:
                        new_members = self.members | skill.members
                        if len(new_members) <= 5:
                                self.members = new_members
                                self.skills.add(skill)
                                self.up = sum(self.skills) + 1.0

        def merge(self, team):
                if self.leader == team.leader:
                        new_members = self.members | team.members
                        if len(new_members) <= 5:
                                self.members = new_members
                                self.skills |= team.skills
                                self.up = sum(self.skills) + 1.0
       
        def __str__(self):
                s = 'team: ('
                for m in self.members:
                        if self.leader is not None and m == self.leader:
                                s += '[' + str(m) + '], '
                        else:
                                s += str(m) + ', '
                s += str(self.up) + ' )' 

                return s

