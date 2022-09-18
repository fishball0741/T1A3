import random
import zombie
import Choose


Boomer = zombie.Boss('LV.1_Boomer', health=200, attack=6)
Hunter = zombie.Boss('LV.2_Hunter', health=150, attack= 20)
Witch = zombie.Boss('LV.3_Witch', health=250, attack=25)
Tank = zombie.Boss('Final_Tank', health=350, attack=30)

boss_dmg = random.randint(0, Boomer.attack)
name_dmg = random.randint(10, Choose.choose_character)


def play_game():

    if name.health > 0:
        boss_dmg = random.randint(0, Boomer.attack)
    elif boss.health > 0:
        name_dmg = random.randint(10, gender.attack) 
    elif name.health == 0:
        end_game()
    elif zombie.Boss.health == 0:
        win_game()

def end_game():
    print("your health reach 0, game over")
    user_input= input("Do you want to start a new game? ")
    if(user_input == "yes"):
        new_game()

def win_game():
    print("Congrat, you win!")
    user_input= input("Do you want to go the next level? ")
    if(user_input == "yes"):
        next_level()


def new_game():
    Choose.choose_character()
    play_game()

def next_level():
    play_game()


name_dmg.__dict__