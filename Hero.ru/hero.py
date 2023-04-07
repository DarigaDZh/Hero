class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.named = name
        self.nicknamed = nickname
        self.superpowerd = superpower
        self.health_pointsd = health_points
        self.catchphrased = catchphrase

    def print_name(self):
        print(f"My name is {self.named}")

    def double_health_points(self):
        self.health_pointsd *= 2

    def __str__(self):
        return f"{self.nicknamed} has the superpower of {self.superpowerd} and currently has {self.health_pointsd} health points."

    def __len__(self):
        return len(self.catchphrased)
# Создаем объект класса SuperHero
hero = SuperHero(name='Bruce Wayne', nickname='batman', superpower='money', health_points=80, catchphrase='I am whatever Gotham needs me to be')
print(hero)

