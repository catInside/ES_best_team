# -*- coding: utf-8 -*- 

# from team_set import Team_Set



class Character(object):
        def __init__(self, name):
                self.name = name
                self.cards = []
                self.skills = set()
                self.teams = set()

        def add_card(self, card):
                if card.char_name == self.name:
                        self.cards.append(card)
                        self.cards.sort(reverse = True)
                
        def add_skill(self, skill):
                if self.name in skill:
                        self.skills.add(skill)

        def add_team(self, team):
                if self == team.leader:
                        self.teams.add(team)

        def __str__(self):
                return self.name
