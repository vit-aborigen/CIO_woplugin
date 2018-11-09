isDebug = True

def log(text):
    if isDebug:
        print(text)


class Army(object):
    def __init__(self):
        self.units = []

    def add_units(self, unit_type, amount):
        self.units.extend([unit_type() for i in range(amount)])

    def get_units(self):
        if len(self):
            return self.units.pop(0)

    def check_next_unit(self):
        if len(self):
            return self.units[0]

    def __len__(self):
        return len(self.units)


class Battle(object):
    def __init__(self):
        self.army_1 = self.army_2 = None

    def fight(self, army_1, army_2):
        self.army_1 = army_1
        self.army_2 = army_2
        log("\nInitial")
        unit_1 = army_1.get_units()
        unit_2 = army_2.get_units()

        while unit_1.is_alive and unit_2.is_alive:
            if self.fight_between_units(unit_1, unit_2):
                if len(army_2) > 0:
                    log('\nNew unit from the army_2. {} units left'.format(len(army_2)))
                    unit_2 = army_2.get_units()
            elif len(army_1) > 0:
                log('\nNew unit from the army_1. {} units left'.format(len(army_1)))
                unit_1 = army_1.get_units()
        return unit_1.is_alive

    def fight_between_units(self, unit_1, unit_2):
        while all([unit_1.is_alive, unit_2.is_alive]):
            log("{} HP: {:2d}, {} HP: {:2d}".format(unit_1, unit_1.health, unit_2, unit_2.health))
            unit_3 = self.army_2.check_next_unit() if self.army_2 else None
            self.calculate_damage_done(unit_1, unit_2, unit_3)
            if unit_2.is_alive:
                unit_3 = self.army_1.check_next_unit() if self.army_1 else None
                self.calculate_damage_done(unit_2, unit_1, unit_3)
        return unit_1.is_alive

    @staticmethod
    def calculate_damage_done(unit_1, unit_2, unit_3=None):
        damage_dealt = max(unit_1.attack - unit_2.defence, 0)
        unit_2.health -= damage_dealt

        if isinstance(unit_1, Vampire):
            unit_1.drain(damage_dealt)

        if isinstance(unit_1, Lancer):
            if unit_3:
                damage_dealt = max(unit_1.attack - unit_3.defence, 0)
                unit_1.splash(damage_dealt, unit_3)


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.defence = 0
        self.vampirism = 0
        self.collateral = 0

    def __str__(self):
        return type(self).__name__

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
        unit.health -= int(damage_done * self.collateral)


fight = Battle().fight_between_units

if __name__ == '__main__':
    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Lancer, 5)
    army_1.add_units(Vampire, 3)
    army_1.add_units(Warrior, 4)
    army_1.add_units(Defender, 2)
    army_2.add_units(Warrior, 4)
    army_2.add_units(Defender, 4)
    army_2.add_units(Vampire, 6)
    army_2.add_units(Lancer, 5)
    battle = Battle()
    print(battle.fight(army_1, army_2))
    print("Coding complete? Let's try tests!")