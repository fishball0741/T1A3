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
    
