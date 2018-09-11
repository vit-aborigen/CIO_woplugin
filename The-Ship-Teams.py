def two_teams(sailors):
    team_one = sorted([sailor for sailor in sailors if 20 <= sailors[sailor] <= 40])
    team_two = sorted([sailor for sailor in sailors.keys() if sailor not in team_one])
    return [team_two, team_one]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert two_teams({
        'Smith': 34,
        'Wesson': 22,
        'Coleman': 45,
        'Abrahams': 19}) == [
            ['Abrahams', 'Coleman'],
            ['Smith', 'Wesson']
            ]

    assert two_teams({
        'Fernandes': 18,
        'Johnson': 22,
        'Kale': 41,
        'McCortney': 54}) == [
            ['Fernandes', 'Kale', 'McCortney'],
            ['Johnson']
            ]
    print("Coding complete? Click 'Check' to earn cool rewards!")
