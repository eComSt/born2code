class Animal:
    def walk(self):
        print('im walk')
    def say(self):
        print('im say')
        
class Bird(Animal):
    def walk(self):
        print('im fly')
        super().walk()
        
a = Bird()
a.say()