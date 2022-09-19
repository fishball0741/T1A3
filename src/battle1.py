import random
import zombie
import Choose

# male = zombie.Character('Raymond', health=130, attack=10)
# female = zombie.Character('Becky', health=90, attack=20)
# Boomer = zombie.Boss('LV.1_Boomer', health=200, attack=6)
# Hunter = zombie.Boss('LV.2_Hunter', health=150, attack= 20)
# Witch = zombie.Boss('LV.3_Witch', health=250, attack=25)
# Tank = zombie.Boss('Final_Tank', health=350, attack=30)


def next_level():
    first_game()


def first_game():
    Choose.choose_character()
    Boomer = zombie.Boss('LV.1_Boomer', health=200, attack=6)
    male = zombie.Character('Raymond', health=130, attack=10)
    female = zombie.Character('Becky', health=90, attack=20)

    while True:
        if male.health > 0 and Boomer.health > 0:
            male.health -= random.randint(0, Boomer.attack)
            print(f'You got hit and only have {male.health} hp left. ')
            Boomer.health -= random.randint(5, male.attack)
            print(f'You successfully hit the Boss and only {Boomer.health} hp left. ')
            continue
        # elif Boomer.health > 0:
        #     Boomer.health -= random.randint(10, male.attack)
        #     print(f'You successfully hit the Boss and only {Boomer.health} left. ')
            
        elif male.health <= 0:
            end_game()
            break
        elif Boomer.health <= 0:
            win_game()
            break
        else:
            if female.health > 0 and Boomer.health > 0:
                female.health -= random.randint(0, Boomer.attack)
                print(f'You got hit and only have {female.health} left. ')
                Boomer.health -= random.randint(10, female.attack)
                print(f'You successfully hit the Boss and only {Boomer.health} left. ')
                continue
            elif female.health <= 0:
                end_game()
                break
            elif Boomer.health <= 0:
                win_game()
                break


def end_game():
    print("your health reach 0, game over")
    # user_input= input("Do you want to start a new game? ")
    # if(user_input == "yes"):
    #     first_game()

def win_game():
    print("Congrat, you win!")
    # user_input= input("Do you want to go the next level? ")
    # if(user_input == "yes"):
    #     next_level()


first_game()