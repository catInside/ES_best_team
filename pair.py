# -*- coding: utf-8 -*- 

import copy



class Pair(object):
        def __init__(self, team1, team2, cards):
                self.team1 = max(team1, team2)
                self.team2 = min(team1, team2)
                self.cards1 = []
                self.cards2 = []
                self.points = 0
                self.get_best_cards(cards)

        def __eq__(self, other):
                return self.cards1 == other.cards1 and self.cards2 == other.cards2

        def __ne__(self, other):
                return self.cards1 != other.cards1 or self.cards2 != other.cards2

        def has_same_char(self, card):
                for c in self.cards1 + self.cards2:
                        if c.char_name == card.char_name:
                                return True
                else:
                        return False

        def get_best_cards(self, cards):
                valid_cards = list(cards)

                for char in self.team1.members:
                        if len(char.cards) <= 0:
                                self.cards1 = []
                                return
                        c = char.cards[0]
                        self.cards1.append(c)
                        valid_cards.remove(c)
                
                while len(self.cards1) < 5:
                        c = max(valid_cards)
                        valid_cards.remove(c)
                        if not self.has_same_char(c) and (c.char not in self.team2 or len(c.char.cards) > 1):
                                self.cards1.append(c)

                valid_cards = list(cards)
                for c in self.cards1:
                        valid_cards.remove(c)

                for char in self.team2.members:
                        for c in char.cards:
                                if c not in self.cards1:
                                        break
                        else:
                                self.cards2 = []
                                return
                        self.cards2.append(c)
                        valid_cards.remove(c)

                while len(self.cards2) < 5:
                        c = max(valid_cards)
                        self.cards2.append(c)
                        valid_cards.remove(c)

                self.points = sum(self.cards1) * self.team1.up + sum(self.cards2) * self.team2.up

        def __str__(self):
                s = 'pair: ' + str(self.points) + '\n'
                s += str_of_cards(self.cards1, self.team1)
                s += ',' + str(sum(self.cards1) * self.team1.up) + '\n' 

                s += str_of_cards(self.cards2, self.team2)
                s += ',' + str(sum(self.cards2) * self.team2.up) + '\n' 

                return s

def str_of_cards(cards, team):
        s = 'team: ('
        for m in cards:
                if team.leader is not None and m == team.leader:
                        s += '[' + str(m) + '], '
                else:
                        s += str(m) + ', '
        s += str(team.up) + ' )' 
        return s

