import Choose
import battle
import zombie
import argparse
from sys import argv

parser = argparse.ArgumentParser()
parser.add_argument('--gender',  choices=['m', 'f'], required=False)
args = parser.parse_args()


def main():
    # define all the boss
    lv1_boss = zombie.Character('Boomer', health=200, attack=6)
    lv2_boss = zombie.Character('Hunter', health=150, attack=20)
    lv3_boss = zombie.Character('Witch', health=250, attack=25)
    lv4_boss = zombie.Character('Tank', health=350, attack=30)
    
    # execute the character chose, save
    user = Choose.choose_character(args.gender)

    if user.score >= 0:
        battle.game(lv1_boss, user)
        
    if user.score >= 1:
        battle.game(lv2_boss, user)
        
    if user.score >= 2:
        battle.game(lv3_boss, user)
        
    if user.score >= 3:
        battle.game(lv4_boss, user)
        






if __name__ == '__main__':
    main()
