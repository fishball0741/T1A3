from great_text import great_text
import zombie


# def 2 character for user to choose, and thier traits

def choose_character(genderArg):
    gender= ""
    if genderArg:
        if genderArg == "f":
            gender = 'female'
        else:
            gender = 'male'
    else:
        while gender not in ('male', 'female'):
            gender = input("Please select your character, 'male' or 'female'? ")
        if not gender:
            print("Sorry, I didn't catch that. Enter again: ")      
    
    while True:
        name = input("Please write down your character's name: ")
    
        if gender == 'male':
            user = zombie.Character(name, health=130, attack=10, score=0, max_health=130, max_attack=10)
            print(f'Hi, {name}, your health is {user.health} and attack is {user.attack}. ')
            great_text(f"HP:{user.health}     DMG: {user.attack}","magenta","letterw3")
            break
        elif gender == 'female':
            user = zombie.Character(name, health=90, attack=20, score=0, max_health=90, max_attack=20)
            print(f'Hi, {user.name}, your health is {user.health} and attack is {user.attack}.')
            great_text(f"HP:{user.health}     DMG: {user.attack}","magenta","letterw3")
            break
        else:
            print('Please make sure you type the correct gender for your character. ')
            continue
        
    return user

