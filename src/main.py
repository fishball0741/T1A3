import Choose
import battle
import zombie


def main():
    # define all the boss
    lv1_boss = zombie.Character('Boomer', health=200, attack=6)
    lv2_boss = zombie.Character('Hunter', health=150, attack=20)
    lv3_boss = zombie.Character('Witch', health=250, attack=25)
    lv4_boss = zombie.Character('Tank', health=350, attack=30)
    
    # execute the character chose, save
    user = Choose.choose_character()

    if user.score >= 0:
        battle.game(lv1_boss, user)
        
    if user.score >= 1:
        battle.game(lv2_boss, user)
        
    if user.score >= 2:
        battle.game(lv3_boss, user)
        
    if user.score >= 3:
        battle.game(lv4_boss, user)
        exit()






if __name__ == '__main__':
    main()
