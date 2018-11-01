class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_h = width_WE
        self.width_v = width_NS
        self.height = height

    def return_corners(self):
        NW = [self.south + self.width_v, self.west]
        NE = [self.south + self.width_v, self.west + self.width_h]
        SW = [self.south, self.west]
        SE = [self.south, self.west + self.width_h]
        return (NW, NE, SW, SE)

    def corners(self):
        names = ("north-west", "north-east", "south-west", "south-east")
        return {k: v for k, v in zip(names, self.return_corners())}

    def area(self):
        return self.width_h * self.width_v

    def volume(self):
        return self.area() * self.height

    def __repr__(self):
        return "Building({}, {}, {}, {}, {})".format(self.south, self.west, self.width_h, self.width_v, self.height)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"
