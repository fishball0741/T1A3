import Choose
import battle1
import zombie

# male = zombie.Character('Raymond', health=130, attack=10)
# female = zombie.Character('Becky', health=90, attack=20)
# item = zombie.Item('AK-47', 'Lv.3 Shield', 50)
# Boomer = zombie.Boss('LV.1_Boomer', health=200, attack=6)
# Hunter = zombie.Boss('LV.2_Hunter', health=150, attack= 20)
# Witch = zombie.Boss('LV.3_Witch', health=250, attack=25)
# Tank = zombie.Boss('Final_Tank', health=350, attack=30)

def main():
    # define all the boss
    lv1_boss = zombie.Character('Boomer', health=200, attack=6, score=1)
    lv2_boss = zombie.Character('Hunter', health=150, attack=20, score=2)
    lv3_boss = zombie.Character('Witch', health=250, attack=25, score=3)
    lv4_boss = zombie.Character('Tank', health=350, attack=30, score=4)
    
    # execute the character chose, save
    user = Choose.choose_character()

    



def new_game():
    Choose.choose_character()
    battle1.first_game()

def next_level():
    battle1.first_game()

