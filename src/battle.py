import random
import zombie
import main
import item
from great_text import great_text


def end_game():
    great_text("Game Over","red","colossal")

    print("your health reach 0, game over")
    user_input= input("Do you want to start a new game? 'yes' or 'no' ")
    if(user_input == "yes"):
        main.main()
    else:
        print("Please typr the correct answer, 'yes' or 'no' ? ")        

def win_game(user: zombie.Character):
    great_text("YOU WON","cyan","chunky")
    print(f"Congrat, you win and you earn {user.score+1} points. ")
    item.item(user)
    user.max_health += 10
    user.max_attack += 8
    user.attack = user.max_attack
    user.health = user.max_health
    print(f'And you now are level up, your health is {user.health} and your attack is {user.attack} ')
    great_text(f"HP:{user.health}     DMG: {user.attack}","magenta","letterw3")
    while True:
        user_input= input("Do you want to go the next level? 'yes' or 'no' ")
        if(user_input == "yes"):
            user.score += 1
            break
        elif (user_input == "no"):
            print("Thanks for playing, see you next time:)")
            exit()
        else:
            print("Please type the correct answer, 'yes' or 'no' ? ")
            continue
        

def game(boss: zombie.Character, user: zombie.Character):
    print(f"the boss name is {boss.name} who has {boss.health} hp and {boss.attack} dmg, GOOD LUCK and LET's FIGHT!!! ")
    while True:
        if user.health > 0 and boss.health > 0:
            user.health -= random.randint(0, boss.attack)
            print(f'You got hit and only have {user.health} hp left. ')
            boss.health -= random.randint(5, user.attack)
            print(f'You successfully hit the Boss and only {boss.health} hp left. ')
            continue
          
        elif user.health <= 0:
            end_game()
            break
        elif boss.health <= 0:
            win_game(user)
            break
        
def final():
    game()



        



