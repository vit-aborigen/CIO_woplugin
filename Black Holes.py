from math import pi, hypot, acos, sqrt

class Black_hole:
    def __init__(self, data):
        self.x = data[0]
        self.y = data[1]
        self.radius = data[2]

    @property
    def area(self):
        return pi * self.radius ** 2

    def find_distance_to_another_hole(self, another_hole):
        return hypot(another_hole.x - self.x, another_hole.y - self.y)

    def absorb_another_hole(self, another_hole):
        new_area = self.area + another_hole.area
        self.radius = round(sqrt(new_area / pi), 2)

    def __str__(self):
        return 'Hole with radius={} at ({};{})'.format(self.radius, self.x, self.y)

    __repr__ = __str__


class State:
    def __init__(self, holes):
        self.holes = [Black_hole(hole) for hole in holes]
        self.checked_pairs = set()

    def find_closest_holes(self):
        best_pair = [404, 0, 0]
        for idx, hole_1 in enumerate(self.holes):
            for hole_2 in self.holes[idx + 1:]:
                if (hole_2, hole_1) in self.checked_pairs or (hole_1, hole_2) in self.checked_pairs:  continue
                distance = hole_1.find_distance_to_another_hole(hole_2)
                if distance < best_pair[0]:
                    leftmost = sorted([hole_1, hole_2], key=lambda black_hole: black_hole.x)
                    best_pair = [distance,] + leftmost
        return best_pair


    def find_intersection_between_holes_by_sim0000(self, hole_1, hole_2):
        x1, y1, r1 = hole_1.x, hole_1.y, hole_1.radius
        x2, y2, r2 = hole_2.x, hole_2.y, hole_2.radius
        d = hole_1.find_distance_to_another_hole(hole_2)
        if r1 + r2 <= d: return 0
        s = ((2 * d * r1) ** 2 - (d ** 2 + r1 ** 2 - r2 ** 2) ** 2) / 4
        if s <= 0: return min(hole_1.area, hole_2.area)
        th1 = (d ** 2 + r1 ** 2 - r2 ** 2) / (2 * d * r1)
        th2 = (d ** 2 + r2 ** 2 - r1 ** 2) / (2 * d * r2)
        return r1 ** 2 * acos(th1) + r2 ** 2 * acos(th2) - sqrt(s)


    def change_state(self):
        closest_holes = self.find_closest_holes()
        if closest_holes[0] == 404:
            return 0
        hole_1, hole_2 = closest_holes[1:]
        self.checked_pairs.add((hole_1, hole_2))
        intersection = self.find_intersection_between_holes_by_sim0000(hole_1, hole_2)
        hole_1_inters, hole_2_inters = intersection / hole_1.area, intersection / hole_2.area
        if hole_1_inters >= 0.55 or hole_2_inters >= 0.55:
            if hole_1.area / hole_2.area >= 1.2:
                hole_1.absorb_another_hole(hole_2)
                self.holes.remove(hole_2)
                self.checked_pairs = set()
            elif hole_2.area / hole_1.area >= 1.2:
                hole_2.absorb_another_hole(hole_1)
                self.holes.remove(hole_1)
                self.checked_pairs = set()
        return 1


def checkio(data):
    state = State(data)
    while state.change_state():
        continue
    return [(hole.x, hole.y, hole.radius) for hole in state.holes]

print(checkio([[0.8,0,1],[1,0,1],[1.5,0,0.5]]))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([(2, 4, 2), (3, 9, 3)]) == [(2, 4, 2), (3, 9, 3)]
    assert checkio([(0, 0, 2), (-1, 0, 2)]) == [(0, 0, 2), (-1, 0, 2)]
    assert checkio([(4, 3, 2), (2.5, 3.5, 1.4)]) == [(4, 3, 2.44)]
    assert checkio([(3, 3, 3), (2, 2, 1), (3, 5, 1.5)]) == [(3, 3, 3.5)]
