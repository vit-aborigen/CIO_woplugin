class Army(object):
    def __init__(self):
        self.units = []

    def add_units(self, unit_type, amount):
        self.units.extend([unit_type() for i in range(amount)])

    def __len__(self):
        return len(self.units)

class Battle(object):
    def fight(self, army_1, army_2):
        unit_1 = army_1.units.pop(0)
        unit_2 = army_2.units.pop(0)

        while unit_1.is_alive and unit_2.is_alive:
            if fight(unit_1, unit_2):
                if len(army_2) > 0:
                    unit_2 = army_2.units.pop(0)
            elif len(army_1) > 0:
                unit_1 = army_1.units.pop(0)

        return unit_1.is_alive


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return True if self.health > 0 else False

class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7

def fight(unit_1, unit_2):
    while all([unit_1.is_alive, unit_2.is_alive]):
        unit_2.health -= unit_1.attack
        if unit_2.is_alive:
            unit_1.health -= unit_2.attack
    return unit_1.is_alive


if __name__ == '__main__':
    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Warrior, 10)
    army_2.add_units(Warrior, 11)
    battle = Battle()
    assert battle.fight(army_1, army_2) == True
