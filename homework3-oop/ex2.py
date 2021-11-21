"""
    Create 3 classes:
        - Cat
        - Dog
        - Mouse

    All of these 3 classes must inherit from the Animal class.

    public attributes:
        - inherited from Animal (on init (or also called constructor))
        - enemy (on constructor (init))
            - is reference to the enemy of the current Animal
            e.g. Dog is the enemy of Cat

    private attributes:
        - specific_sound: str

    public methods:
        - inherited from Animal

    private methods:
        - enemy_fear_sound() - returns str
            - this is called inside the sound() method, and if an enemy has
            been passed on the constructor, then the sound should be different
            than the usual sound of the animal

            e.g.
                if Cat is called with enemy = Dog, then the cat should make
            a "meoooooow scared" sound.
                else the cat makes a "meow" sound
"""

from ex1 import Animal, AnimalTypeEnum


class Dog(Animal):
    def __init__(self, color: str, age: int, enemy=None):
        super().__init__(color, age, AnimalTypeEnum.DOG)
        self.enemy = enemy
        self.__specific_sound = 'wooof'

    def __enemy_fear_sound(self):
        return 'Woof Scared'

    def sound(self):
        if self.enemy == Mouse:
            return self.__enemy_fear_sound()
        else:
            return self.__specific_sound

    def tell_age(self):
        return self.age

    def age_up(self):
        self.age = self.age + 1


class Cat(Animal):
    def __init__(self, color: str, age: int, enemy=None):
        super().__init__(color, age, AnimalTypeEnum.CAT)
        self.enemy = enemy
        self.__specific_sound = 'meoow'

    def __enemy_fear_sound(self):
        return 'Meeoow Scared'

    def sound(self):
        if self.enemy == Dog:
            return self.__enemy_fear_sound()
        else:
            return self.__specific_sound

    def tell_age(self):
        return self.age

    def age_up(self):
        self.age = self.age + 1


class Mouse(Animal):
    def __init__(self, color: str, age: int, enemy=None):
        super().__init__(color, age, AnimalTypeEnum.MOUSE)
        self.enemy = enemy
        self.__specific_sound = 'Kitkit'

    def __enemy_fear_sound(self):
        return 'kit kit Scared'

    def sound(self):
        if self.enemy == Cat:
            return self.__enemy_fear_sound()
        else:
            return self.__specific_sound

    def tell_age(self):
        return self.age

    def age_up(self):
        self.age = self.age + 1


animal1 = Dog('black', 1, Mouse)
animal2 = Cat('red', 4, Dog)
animal3 = Mouse('grey', 10, Dog)


print(animal1.sound())
print(animal2.sound())
print(animal3.sound())
