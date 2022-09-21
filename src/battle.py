import random
import zombie
import main
import Choose

def end_game():
    print("your health reach 0, game over")
    user_input= input("Do you want to start a new game? 'yes' or 'no' ")
    if(user_input == "yes"):
        main.main()

def win_game(user: zombie.Character):
    print(f"Congrat, you win and you earn {user.score} points. ")
    user_input= input("Do you want to go the next level? 'yes' or 'no' ")
    if(user_input == "yes"):
        user.score += 1
        user.max_health += 20
        user.attack += 10
        user.health = user.max_health
        print(f'You now are level up, your health is {user.health} and your attack is {user.attack} ')

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





        



