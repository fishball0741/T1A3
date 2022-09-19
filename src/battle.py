import random
import zombie
import main

# male = zombie.Character('Raymond', health=130, attack=10)
# female = zombie.Character('Becky', health=90, attack=20)
# Boomer = zombie.Boss('LV.1_Boomer', health=200, attack=6)
# Hunter = zombie.Boss('LV.2_Hunter', health=150, attack= 20)
# Witch = zombie.Boss('LV.3_Witch', health=250, attack=25)
# Tank = zombie.Boss('Final_Tank', health=350, attack=30)




def play_game():
    Boomer = zombie.Boss('LV.1_Boomer', health=200, attack=6)
    male = zombie.Character('Raymond', health=130, attack=10)
    # female = zombie.Character('Becky', health=90, attack=20)

    while True:
        if male.health > 0 and Boomer.health > 0:
            male.health -= random.randint(0, Boomer.attack)
            print(f'You got hit and only have {male.health} left. ')
            Boomer.health -= random.randint(10, male.attack)
            print(f'You successfully hit the Boss and only {Boomer.health} left. ')
            continue
        # elif Boomer.health > 0:
        #     Boomer.health -= random.randint(10, male.attack)
        #     print(f'You successfully hit the Boss and only {Boomer.health} left. ')
            
        elif male.health <= 0:
            end_game()
            break
        else:
            win_game()
            break

def end_game():
    print("your health reach 0, game over")
    # user_input= input("Do you want to start a new game? ")
    # if(user_input == "yes"):
    #     main.new_game()

def win_game():
    print("Congrat, you win!")
    # user_input= input("Do you want to go the next level? ")
    # if(user_input == "yes"):
    #     main.new_game()


play_game()