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
            male = zombie.Character(name, health=130, attack=10, score=0)
            print(f'Hi, {male.name}, your health is {male.health} and attack is {male.attack}. ')
            break
        elif gender == 'female':
            female = zombie.Character(name, health=90, attack=20, score=0)
            print(f'Hi, {female.name}, your health is {female.health} and attack is {female.attack}.')
            break
        else:
            print('Please make sure you type the correct gender for your character. ')
            continue
        


choose_character()
