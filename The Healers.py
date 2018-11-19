isDebug = True
def log(text):
    if isDebug:
        print(text)

class Army(object):
    def __init__(self):
        self.units = []

    def add_units(self, unit_type, amount):
        self.units.extend([unit_type() for i in range(amount)])

    def get_unit(self):
        if len(self):
            return self.units.pop(0)

    def prepare_next_unit(self):
        if len(self):
            return self.units[0]

    def __len__(self):
        return len(self.units)


class Battle(object):
    pass


class Warrior:
    def __init__(self):
        self.max_health = 50
        self.current_health = self.max_health
        self.attack = 5
        self.defence = 0
        self.vampirism = 0
        self.collateral = 0
        self.heal = 0

    def __str__(self):
        return type(self).__name__ + ' with ' + self.current_health + ' HP'

    @property
    def is_alive(self):
        return True if self.current_health > 0 else False


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defence = 2


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 0.5

    def drain(self, damage_done):
        self.health += int(damage_done * self.vampirism)


class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 6
        self.collateral = 0.5

    def splash(self, damage_done, unit):
        unit.current_health -= int(damage_done * self.collateral)


class Healer(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 0
        self.heal = 2

    def heal(self, unit):
        unit.current_heath = min(unit.max_health, unit.current_heath + 2)