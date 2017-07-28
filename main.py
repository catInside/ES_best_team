# -*- coding: utf-8 -*- 
# Author: Huangxin
# Last Update: 2017_7_18


from itertools import combinations

from data_skills import red_skills, yellow_skills, blue_skills
from data_cards import red_cards, yellow_cards, blue_cards
from data_characters import characters as chars_dict

from card import Card
from skill import Skill
from character import Character
from team import Team
from pair import Pair
# from team_set import Team_Set


def main():
        find_best_team(red_cards, red_skills)
        find_best_team(yellow_cards, yellow_skills)
        find_best_team(blue_cards, blue_skills)

def unserialize(cards_dict, skills_dict):
        chars = {}
        for name in chars_dict.itervalues():
                chars[name] = Character(name)

        cards = []
        for name, (points, char_name) in cards_dict.iteritems():
                card = Card(name, points, char_name)
                char = chars[card.char_name]
                char.add_card(card)
                card.add_char(char)
                cards.append( card )

        skills = []
        for name, (names, up) in skills_dict.iteritems():
                skill = Skill(name, names, up)
                for name in skill.member_names:
                        char = chars[name]
                        char.add_skill(skill)
                        skill.add_char(char)
                skills.append( skill )

        return chars, cards, skills

def find_best_team(cards_dict, skills_dict):
        chars, cards, skills = unserialize(cards_dict, skills_dict)

        simple_teams = find_teams_of_single_skill(skills)

        composite_teams = find_teams_of_merged_skills(chars, simple_teams)

        best_pair = make_completed_team_pairs_and_get_best(composite_teams, cards)

        print_chinease(str(best_pair))


def find_teams_of_single_skill(skills):
        teams = set()
        for skill in skills:
                for char in skill.members:
                        team = Team(char)
                        team.add_skill_members(skill)
                        teams.add(team)
                        char.add_team(team)
        print '[hx] simple_teams', len(teams)

        return team

def find_teams_of_merged_skills(chars, simple_teams):
        teams = set()

        for c in chars.itervalues():
                teams_num = len(c.teams)
                for i in xrange(1, teams_num + 1):
                        for comb in combinations(c.teams, i):
                                team = Team(c)
                                for t in comb:
                                        team.merge(t)
                                teams.add(team)
                                # c.add_team(team)

        teams.add(Team(None))
        print '[hx] composite_teams', len(teams)

        return teams

def make_completed_team_pairs_and_get_best(composite_teams, cards):
        max_points = 0
        best_pair = None

        for comb in combinations(composite_teams, 2):
                pair = Pair(comb[0], comb[1], cards)
                if pair.points > max_points:
                        max_points = pair.points
                        best_pair = pair
        for t in composite_teams:
                pair = Pair(t, t, cards)
                if pair.points > max_points:
                        max_points = pair.points
                        best_pair = pair

        return best_pair


def print_chinease(string):
        print string.decode('utf-8')



if __name__ == '__main__':
        main()
        # team = []
        # cards_list = []
        # for name, (point, char) in red_cards.iteritems():
        #         card = Card(name, point, char)
        #         cards_list.append(card)

        # for i in xrange(len(cards_list)):
        #         team.append(cards_list[i])

        # print 'before'
        # print '(',
        # for m in team:
        #         print str(m).decode('utf-8'),
        # print ')' 

        # team.sort()

        # print 'after'
        # print '(',
        # for m in team:
        #         print str(m).decode('utf-8'),
        # print ')' 