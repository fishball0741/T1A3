import zombie





# male = zombie.Character('Raymond', health=130, attack=10)
# female = zombie.Character('Becky', health=90, attack=20)

# def 2 character for user to choose, and thier traits
def choose_character():
    
    while True:
        # male = zombie.Character('Raymond', health=130, attack=10, score=0)
        # female = zombie.Character('Becky', health=90, attack=20, score=0)
        # input to choose male / female
        gender = input("Please select your character, 'male' or 'female'? ")
        name = input("Please write down your character's name: ")
    
        if gender == 'male':
            user = zombie.Character(name, health=130, attack=10, score=0, max_health=130, max_attack=10)
            print(f'Hi, {name}, your health is {user.health} and attack is {user.attack}. ')
            break
        elif gender == 'female':
            user = zombie.Character(name, health=90, attack=20, score=0, max_health=90, max_attack=20)
            print(f'Hi, {user.name}, your health is {user.health} and attack is {user.attack}.')
            break
        else:
            print('Please make sure you type the correct gender for your character. ')
            continue
        
    return user

