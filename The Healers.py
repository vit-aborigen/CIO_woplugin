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
        return 0

    def prepare_next_unit(self):
        if len(self):
            return self.units[0]
        return 0

    def __len__(self):
        return len(self.units)


class Battle(object):
    def __init__(self):
        self.army_1 = self.army_2 = None

    def fight(self, army_1, army_2):
        self.army_1 = army_1
        self.army_2 = army_2
        log('\nArmy 1: {} units left, Army 2: {} units left'.format(len(army_1), len(army_2)))
        return self.fight_between_armies(army_1, army_2)

    @staticmethod
    def fight_between_units(unit_1, unit_2, ally_1 = None, ally_2 = None):
        while all([unit_1.is_alive, unit_2.is_alive]):
            log("{} HP: {:2d} (attacker) vs {} HP: {:2d} (defender)".format(unit_1, unit_1.health, unit_2, unit_2.health))
            Battle.calculate_damage_done(unit_1, unit_2, ally_2)
            if unit_2.is_alive:
                log("{} HP: {:2d} (defender) vs {} HP: {:2d} (attacker)".format(unit_1, unit_1.health, unit_2, unit_2.health))
                Battle.calculate_damage_done(unit_2, unit_1, ally_1)
        return unit_1.is_alive

    @staticmethod
    def calculate_damage_done(unit_1, unit_2, ally_2 = None):
        damage_dealt = max(unit_1.attack - unit_2.defence, 0)
        unit_2.health -= damage_dealt

        if isinstance(unit_1, Vampire):
            unit_1.drain(damage_dealt)

        if isinstance(unit_1, Lancer):
            if ally_2:
                damage_dealt = max(unit_1.attack - ally_2.defence, 0)
                unit_1.splash(damage_dealt, ally_2)

        if isinstance(ally_2, Healer):
            if ally_2:
                ally_2.heal(unit_2)

    def fight_between_armies(self, army_1: Army, army_2: Army):
        self.army_1 = army_1
        self.army_2 = army_2

        unit_1 = army_1.get_unit()
        unit_2 = army_2.get_unit()
        ally_1 = army_1.prepare_next_unit()
        ally_2 = army_1.prepare_next_unit()

        while (unit_1.is_alive or len(army_1)) and (unit_2.is_alive or len(army_2)):
            fight_result = Battle.fight_between_units(unit_1, unit_2, ally_1, ally_2)
            if fight_result:
                if len(army_2) > 0:
                    unit_2 = army_2.get_unit()
                    ally_2 = army_2.prepare_next_unit()
                    log('\nNew unit from the army_2. Army 1: {} units left, Army 2: {} units left'.format(len(army_1), len(army_2)))
            elif len(army_1) > 0:
                unit_1 = army_1.get_unit()
                ally_1 = army_1.prepare_next_unit()
                log('\nNew unit from the army_1. Army 1: {} units left, Army 2: {} units left'.format(len(army_1), len(army_2)))

        print(len(army_1), len(army_2))
        return unit_1.is_alive


class Warrior:
    def __init__(self):
        self.max_health = 50
        self.health = self.max_health
        self.attack = 5
        self.defence = 0
        self.vampirism = 0
        self.collateral = 0
        self.heal_power = 0

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
        self.max_health = 60
        self.health = self.max_health
        self.attack = 3
        self.defence = 2


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.max_health = 40
        self.health = self.max_health
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


class Healer(Warrior):
    def __init__(self):
        super().__init__()
        self.max_health = 60
        self.health = self.max_health
        self.attack = 0
        self.heal_power = 2

    def heal(self, unit):
        unit.health = min(unit.max_health, unit.health + self.heal_power)


fight = Battle.fight_between_units