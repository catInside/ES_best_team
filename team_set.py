# -*- coding: utf-8 -*- 



class Team_Set(object):
        def __init__(self):
                self.elements = []

        def __contains__(self, element):
                for e in self.elements:
                        if e == element:
                                return True
                else:
                        return False

        def __eq__(self, other):
                return self.issubset(other) and other.issubset(self)

        def __ne__(self, other):
                return not self.issubset(other) or not other.issubset(self)

        def __ior__(self, other):
                for e in other.elements:
                        self.add(e)

        def __or__(self, other):
                s = Team_Set()
                for e in self.elements:
                        s.elements.append(e)
                for e in other.elements:
                        s.add(e)

        def __len__(self):
                return len(self.elements)

        def __iter__(self):
                return self.elements.__iter__()
                               
        def add(self, element):
                for e in self.elements:
                        if e == element:
                                e.skills = max(e, element).skills
                                e.up = max(e, element).up
                else:
                        self.elements.append(element)

        def issubset(self, other):
                for e in other.elements:
                        if e not in self.elements:
                                return False
                else:
                        return True
