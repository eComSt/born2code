from random import randint

class Human:
    def __init__(self, name: str, health: int):
        self._name = name
        self._health = health
        self._max_health = health

    def attack(self, enemy):
        damage_value = randint(1, 10)
        print(f"{self._name} наносит персонажу {enemy._name} {damage_value} урона!")
        enemy.get_damage(damage_value)

    def get_damage(self, damage):
        self._health -= damage
        print(f"{self._name} получает {damage} урона! Текущее здоровье — {self._health}.")

    def healing(self):
        heal_value = randint(1, 15)
        if self._health + heal_value >= self._max_health:
            print(f"{self._name} восстанавливает {self._max_health - self._health} здоровья. Текущее здоровье — {self._max_health}.")
            self._health = self._max_health
        else:
            print(f"{self._name} восстанавливает {heal_value} здоровья. Текущее здоровье — {self._health + heal_value}.")
            self._health += heal_value

class Warrior(Human):
    def __init__(self, name: str, health: int, defense: float):
        super().__init__(name=name, health=health)
        self._defense = defense

    def attack(self, enemy):
        damage_value = randint(10, 20)
        print(f"{self._name} наносит персонажу {enemy._name} {damage_value} урона!")
        enemy.get_damage(damage_value)

    def get_damage(self, damage):
        damage = max(damage - self._defense, 0)
        if self._health - damage > 0:
            self._health -= damage
            print(f"{self._name} получает {damage} урона! Текущее здоровье — {self._health}.")
        else:
            print(f"{self._name} получает {self._health} урона! Текущее здоровье — 0.")
            self._health = 0      

class Archer(Human):
    def __init__(self, name: str, health: int, accuracy: float, agility: int):
        super().__init__(name=name, health=health)
        self._accuracy = accuracy
        self._agility = agility

    def attack(self, enemy):
        damage_value = randint(15, 25) * self._accuracy
        print(f"{self._name} наносит персонажу {enemy._name} {damage_value} урона!")
        enemy.get_damage(damage_value)
    
    def get_damage(self, damage):
        if randint(1, 100) <= self._agility:
            print(f"«{self._name} увернулся от удара!»")
        else:
            self._health -= damage
            print(f"{self._name} получает {damage} урона! Текущее здоровье — {self._health}.")        

human = Human(name="Стив", health=80)
warrior = Warrior(name="Артур", health=120, defense=5)
archer = Archer(name="Робин", health=15, accuracy=1.15, agility=10)

human.attack(warrior)
warrior.attack(archer)
archer.healing()