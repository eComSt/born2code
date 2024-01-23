class Knight:
    name = ''
    health = 0
    stamina = 0
    armor_level = 0
    damage = 0

my_knight = Knight()

my_knight.name = 'Sir Arthur'
my_knight.health = 100
my_knight.stamina = 60
my_knight.armor_level = 10
my_knight.damage = 20


class Knight:
    name = ''
    hp = 0
    stamina = 0
    armor = 0
    dmg = 0

knight_char = []


knight = Knight()

knight.name = input("Введите имя персонажа: ")
knight.hp = int(input("Введите здоровье персонажа: "))
knight.stamina = int(input("Введите уровень выносливости персонажа: "))
knight.armor = int(input("Введите уровень брони персонажа: "))
knight.dmg = int(input("Введите урон персонажа: "))
knight_char.append(knight)
print("----------------------------------")

print(knight_char)

for knight in knight_char:
    print(f"Имя: {knight.name}")
    print(f"Здоровье: {knight.hp}")
    print(f"Выносливость: {knight.stamina}")
    print(f"Броня: {knight.armor}")
    print(f"Урон: {knight.dmg}")
    
class Knight:
    Name = ' '
    HP = 0
    EP = 0
    Armor = 0
    Damage = 0
charact = Knight()
charact.Name = input('Введите имя:')
charact.HP = int(input('Введите количество очков здоровья:'))
charact.EP = int(input('Введите количество очков выносливости:'))
charact.Armor = int(input('Введите уровень брони:'))
charact.Damage = int(input('Введите наносимый урон:'))
print('◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆')
print('Ваш персонаж:')
print (f'Имя:{charact.Name}')
print(f'Здоровье:{charact.HP}')
print (f'Выносливость:{charact.EP}')
print (f'Броня:{charact.Armor}')
print (f'Урон:{charact.Damage}')
print('◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆')



class Knight:
    def init(self):
        self.name = ''
        self.health_points = 0
        self.stamina_points = 0
        self.armor_level = 0
        self.damage_points = 0

knight = Knight()
knight.name = 'Sir Lancelot'
knight.health_points = 100
knight.stamina_points = 50
knight.armor_level = 10
knight.damage_points = 20

class Knight:
    name = ''
    health = 0
    stamina = 0
    armor = 0
    damage = 0
hero = Knight()
hero.name = 'Gerald'
hero.health = 100
hero.stamina = 100
hero.armor = 100
hero.damage = 42


class  Knight:
    name = ""
    health = 0
    stamina = 0
    armor_lvl = 0 
    damage = 0

Paladin = Knight()
Paladin.name = "Irving"
Paladin.health = 124
Paladin.stamina = 30
Paladin.armor_lvl = 18
Paladin.damage = 2*2*8