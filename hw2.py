class SuperHero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def get_hp(self):
        return self.hp

    def increase_hp(self):
        self.hp *= 2


class AirHero(SuperHero):
    def __init__(self, name, hp, damage, fly=False):
        super().__init__(name, hp)
        self.damage = damage
        self.fly = fly

    def increase_hp(self):
        self.hp **= 2
        self.fly = True

    def fly_phrase(self):
        if self.fly:
            print(f"{self.name} can fly!")


class EarthHero(SuperHero):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp)
        self.damage = damage
        self.strength = 10

    def increase_hp(self):
        self.hp **= 2
        self.strength *= 2

    def strength_phrase(self):
        print(f"{self.name} has strength of {self.strength}!")


class SpaceHero(SuperHero):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp)
        self.damage = damage
        self.aliens_defeated = 0

    def increase_hp(self):
        self.hp **= 2
        self.aliens_defeated += 1

    def aliens_defeated_phrase(self):
        print(f"{self.name} has defeated {self.aliens_defeated} aliens!")


class Villain(EarthHero):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)
        self.people = 'monster'

    def gen_x(self):
        pass

    def crit(self, damage):
        return damage ** 2
air_hero = AirHero("Wind Tom", 100, 10)
earth_hero = EarthHero("Rock Cris", 100, 20)
space_hero = SpaceHero("Star Evil", 100, 30)
villain = Villain("Evil Monster", 100, 40)
air_hero.increase_hp()
air_hero.fly_phrase()
earth_hero.increase_hp()
earth_hero.strength_phrase()
space_hero.increase_hp()
space_hero.aliens_defeated_phrase()
villain.increase_hp()
villain.strength_phrase()
villain.crit(50)  # Возводит 50 в квадрат
