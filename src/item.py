import zombie
def item(user: zombie.Character):
    while True:
        number = input("Please choose (1-5) to get your reward box. ")
        if not number.isnumeric():
            print("Please type the integer (1-5). ")
        else:
            number = int(number)
            if number == 1:
                number = user.max_attack
                user.max_attack += 15
                user.attack = user.max_attack
                print(f"Congrat, you picked a shortgun and your total dmg is {user.attack} now. ")
                break
            if number == 2:
                number = user.max_health
                user.max_health += 1
                user.health = user.max_health
                print(f"Congrat, you found a helmet and your gain your health to {user.health} now. ")
                break
            if number == 3:
                print("Sorry, you got a empty box, someone already took the thing inside. ")
                break
            if number == 4:
                number = user.max_attack
                user.max_attack += 20
                user.attack = user.max_attack
                print(f"Congrat, you picked a AK-47 and your total dmg is {user.attack} now. ")
                break
            if number == 5:
                number = user.max_health
                user.max_health += 20
                user.health = user.max_health
                print(f"Congrat, you found bullet-proof vest and your gain your health to {user.health} now. ")
                break
            
            else:
                print("Please type the correct number (1-5). ")
                continue


