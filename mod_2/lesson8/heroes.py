# Герои меча и магии

# создаем класса Hero
class Hero:
    # инициализатор класса
    def __init__(self, name, health, damage, defense):
        self.name = name        # имя
        self.health = health    # здоровье
        self.damage = damage    # наносимый урон
        self.defense = defense  # защита

    # получаем статус параметров героя
    def get_status(self):
        print(f'Имя: {self.name}')
        print(f'Здоровье:{self.health}')
        print(f'Урон: {self.damage}')
        print(f'Защита:{self.defense}')
        print('--------------------------------------------------')

    # метод увеличения защиты героя
    def increase_defense(self):
        # если значение защиты меньше 100
        if self.defense * 1.5 < 100:
            # увеличение защиты в 1.5 раза
            self.defense *= 1.5
        else:
            print('Достигнут максимальный уровень защиты!')
        print(f'Текущий уровень защиты: {self.defense}')
        print('--------------------------------------------------')

    # метод нанесения урона по врагу
    def make_damage(self, enemy):
        print(f'Атака по персонажу {enemy.name}!')
        print('--------------------------------------------------')
        # вызываем метод get_damage() у вражеского героя
        enemy.get_damage(self.damage)
        
    # метод получения урона, учитывая защиту
    def get_damage(self, damage):
        # формула поглощенного урона: урон * защита / 100
        absorbed_damage = damage * self.defense / 100
        # вычисление финального урона
        final_damage = damage - absorbed_damage
        print(f'По герою {self.name} нанесли урон {final_damage}!')
        # уменьшение здоровья героя
        self.health -= final_damage
        print('--------------------------------------------------')

# создаем два экземпляра класса Hero
hero_1 = Hero('Артур', 100, 20, 5)
hero_2 = Hero('Робин', 80, 30, 4)

# получаем статус о параметрах Артура 
hero_1.get_status()
# увеличиваем защиту Артура
hero_1.increase_defense()

# получаем статус о параметрах Робина 
hero_2.get_status()
# Робин наносит урон Артуру
hero_2.make_damage(hero_1)

# получаем статус о параметрах Артура  
hero_1.get_status()
