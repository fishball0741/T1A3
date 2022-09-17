import random
import zombie


def new_game():
    choose_character()
    play_game()

def next_level():
    play_game()



def choose_character():
    gender = input('Please select your character, male or female? ')
    name = input('Please enter your name: ')
    if gender == 'male':
        name = zombie.Character(name, health=130, attack=10)
    else:
        gender = 'female'
        name = zombie.Character(name, health=90, attack=20)
    return

def level():
    one = zombie.Boss('LV.1_Boomer', health=200, attack=6)
    two = zombie.Boss('LV.2_Hunter', health=150, attack= 20)
    three = zombie.Boss('LV.3_Witch', health=250, attack=25)
    final = zombie.Boss('Final_Tank', health=350, attack=30)

def play_game(name, one):

    if name.health > 0:
        boss_dmg = random.randint(0, one.attack)
    elif boss.health > 0:
        name_dmg = random.randint(10, name.attack) 
    elif name.health == 0:
        end_game()
    elif zombie.health == 0:
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


print(choose_character)


choose_character()