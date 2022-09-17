import zombie
import random
import Choose


male = zombie.Character('Raymond', health=130, attack=10)
female = zombie.Character('Becky', health=90, attack=20)
item = zombie.Item('AK-47', 'Lv.3 Shield', 50)
Boomer = zombie.Boss('LV.1_Boomer', health=200, attack=6)
Hunter = zombie.Boss('LV.2_Hunter', health=150, attack= 20)
Witch = zombie.Boss('LV.3_Witch', health=250, attack=25)
Tank = zombie.Boss('Final_Tank', health=350, attack=30)


currentGame = zombie.game()
player_health = [male.health, female.health]
player_attack = [male.attack, female.attack]
boss_health = [Boomer.health, Hunter.health, Witch.health, Tank.health]
boss_attack = [Boomer.attack, Hunter.attack, Witch.attack, Tank.attack]
# battle = [male, female, Boomer, Hunter, Witch, Tank]

# print(male.__dict__)
# print(female.__dict__)
# print(item.__dict__)
# print(Boomer.__dict__)
# print(Hunter.__dict__)
# print(Witch.__dict__)
# print(Tank.__dict__)

# print(f'Boomer got hit and still have {Boomer.damage(Tank)} hp left.')

# while player_health <= 0 and boss_health <= 0:
#     player_dmg = random.randint(10, player_attack)
#     boss_dmg = random.randint(0, boss_attack)
#     if player_health > 0:
#         boss_health -= player_dmg
#         print(f'Boomer got hit and still have {boss_health} hp left.')
#     elif boss_health > 0:
#         player_health -= boss_dmg
#         print(f'Male got hit and still have {player_health} hp left.')
# if player_health > 0 and boss_health <= 0:
#     win = True
#     print('Congrat, you WON !!! ')
# elif player_health <= 0 and boss_health > 0:
#     print('GAME OVER!!!')



# print(Boomer.__dict__)