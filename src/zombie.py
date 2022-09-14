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

    def damage(self, Boss):
        points = Boss(self.attack)
        self.health -= points

class Boss(Character):
    def __init__(self, name, health=100, attack=10):
        super().__init__(name, health=health, attack=attack)
    
    def damage(self, Character):
        points = Character(self.attack)
        self.health -= points


class game:
    def __init__(self):
        self.gameOver = False
        self.round = 0

    def newRound(self):
        self.round += 1
        print('\n***   Round: %d   ***\n' %(self.round))  

    def checkWin(self, Character, Boss):
        if Character.health < 1 and Boss.health > 0:
            self.gameOver = True
            print('You Lose~~')
        elif Boss.health < 1 and Character.health > 0:
            self.gameOver = True
            print('You Win!!!')
        elif Character.health < 1 and Boss.health < 1:
            self.gameOver = True
            print('Draw...But you still lose~~')