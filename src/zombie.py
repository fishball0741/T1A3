class Item:
    def __init__(self, weapon, gear):
        self.weapon = weapon
        self.gear = gear
# Human > male and female
class Character:
    def __init__(self, name, health=100, attack=10, score=0, max_health=100):
        self.name = name
        self.health = health
        self.attack = attack
        self.score = score
        self.max_health = max_health


# class Boss(Character):
#     def __init__(self, name, health=100, attack=10):
#         super().__init__(name, health=health, attack=attack)



