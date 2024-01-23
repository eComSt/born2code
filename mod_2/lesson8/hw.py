import random

class Archer:
    def __init__(self, name, health, damage, accuracy, agility):
        self.Name = name
        self.Health = health
        self.Damage = damage
        self.Accuracy = accuracy
        self.Agility = agility

    def stats(self):
        for key, value in self.__dict__.items():
            print(f'{key}: {value}')

    def level_up(self):
        self.Health += 10
        self.Damage += 6

        if self.Accuracy > 2: print('Достигнут лимит Меткости!')
        else: self.Accuracy += 0.05

        if self.Agility > 25: print('Достигнут лимит Ловкости!')
        else: self.Agility += 2

    def land_damage(self, enemy):
        enemy.get_damage(self.Damage * self.Accuracy)

    def get_damage(self, damage):
        if random.randint(1, 100) <= self.Agility: print(f'Лучник {self.Name} увернулся от удара!')
        else: self.Health -= damage