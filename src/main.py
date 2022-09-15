import zombie
import random



male = zombie.Character('Raymond', health=130, attack=10)
female = zombie.Character('Becky', health=90, attack=20)
item = zombie.Item('AK-47', 'Lv.3 Shield', 50)
Boomer = zombie.Boss('LV.1_Boomer', health=200, attack=6)
Hunter = zombie.Boss('LV.2_Hunter', health=150, attack= 20)
Witch = zombie.Boss('LV.3_Witch', health=250, attack=25)
Tank = zombie.Boss('Final_Tank', health=350, attack=30)


currentGame = zombie.game()

battle = [male, female, Boomer, Hunter, Witch, Tank]
# print(male.__dict__)
# print(female.__dict__)
# print(item.__dict__)
# print(Boomer.__dict__)
# print(Hunter.__dict__)
# print(Witch.__dict__)
# print(Tank.__dict__)

print(f'Boomer got hit and still have {Boomer.damage(Tank)} hp left.')


# print(Boomer.__dict__)