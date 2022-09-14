class Item:
    def __init__(self, weapon, gear, potions):
        self.weapon = weapon
        self.gear = gear
        self.potions = potions

# Human > male and female
class Character:
    def __init__(self, name, health=100, attack=10):
        self.name = name
        self.health = health
        self.attack = attack