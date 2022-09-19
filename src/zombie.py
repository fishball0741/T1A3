
class Item:
    def __init__(self, weapon, gear, potions=50):
        self.weapon = weapon
        self.gear = gear
        self.potions = potions

# Human > male and female
class Character:
    def __init__(self, name, health=100, attack=10):
        self.name = name
        self.health = health
        self.attack = attack


class Boss(Character):
    def __init__(self, name, health=100, attack=10):
        super().__init__(name, health=health, attack=attack)



# class Monster:
#     def __init__(self, boomer, hunter, witch, tank):
#         self.boomer = Boss(boomer, health=200, attack=6)
#         self.hunter = Boss(hunter, health=150, attack=20)
#         self.witch = Boss(witch, health=250, attack=25)
#         self.tank = Boss(tank, health=350, attack=30)

# class game:
#     def __init__(self):
#         self.gameOver = False
#         self.round = 0

#     def newRound(self):
#         self.round += 1
#         print('\n***   Round: %d   ***\n' %(self.round))  

#     def checkWin(self, Character, Boss):
#         if Character.health < 1 and Boss.health > 0:
#             self.gameOver = True
#             print('You Lose~~')
#         elif Boss.health < 1 and Character.health > 0:
#             self.gameOver = True
#             print('You Win!!!')
#         elif Character.health < 1 and Boss.health < 1:
#             self.gameOver = True
#             print('Draw...But you still lose~~')

