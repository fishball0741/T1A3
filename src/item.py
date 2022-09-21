import zombie
def item(user: zombie.Character):
    number = int(input("Please choose (1-5) to get your reward box. "))
    if number == 1:
        number = user.max_attack
        user.max_attack += 10
        user.attack = user.max_attack
        print(f"Congrat, you picked a shortgun and your total dmg is {user.attack} now. ")
        
    if number == 2:
        number = user.max_health
        user.max_health += 10
        user.health = user.max_health
        print(f"Congrat, you found a helmet and your gain your health to {user.health} now. ")

    if number == 3:
        print("Sorry, you got a empty box, someone already took the thing inside. ")

    if number == 4:
        number = user.max_attack
        user.max_attack += 20
        user.attack = user.max_attack
        print(f"Congrat, you picked a AK-47 and your total dmg is {user.attack} now. ")

    if number == 5:
        number = user.max_health
        user.max_health += 20
        user.health = user.max_health
        print(f"Congrat, you found bullet-proof vest and your gain your health to {user.health} now. ")



