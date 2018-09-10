isDebug = False

def log(text):
    if isDebug:
        print(text)

class Army(object):
    def __init__(self):
        self.units = []

    def add_units(self, unit_type, amount):
        self.units.extend([unit_type() for i in range(amount)])

    def __len__(self):
        return len(self.units)

class Battle(object):
    def fight(self, army_1, army_2):
        log("Initial")
        unit_1 = army_1.units.pop(0)
        unit_2 = army_2.units.pop(0)

        while unit_1.is_alive and unit_2.is_alive:
            if fight(unit_1, unit_2):
                if len(army_2) > 0:
                    log('\nNew unit from the army_2')
                    unit_2 = army_2.units.pop(0)
            elif len(army_1) > 0:
                log('\nNew unit from the army_1')
                unit_1 = army_1.units.pop(0)

        return unit_1.is_alive


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.defence = 0

    @property
    def is_alive(self):
        return True if self.health > 0 else False

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

def fight(unit_1, unit_2):
    while all([unit_1.is_alive, unit_2.is_alive]):
        log("Unit_1 HP: {:2d}, Unit_2 HP: {:2d}".format(unit_1.health, unit_2.health))
        unit_2.health -= max(unit_1.attack - unit_2.defence, 0)
        if unit_2.is_alive:
            unit_1.health -= max(unit_2.attack - unit_1.defence, 0)
    return unit_1.is_alive


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
