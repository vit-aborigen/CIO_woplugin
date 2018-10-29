class Node(object):
    id = None
    resistance = None

    def __init__(self, number, resistance):
        self.id = number
        self.resistance = resistance
        self.linked_computers = set()
        self.attacker = None

    def add_link(self, pc):
        self.linked_computers.add(pc)

    def get_id(self):
        return self.id

    def attack(self):
        for pc in self.linked_computers:
            if pc.attacker == None:
                pc.attacker = self
            if not pc.is_infected and pc.attacker == self:
                pc.resistance -= 1

    @property
    def is_infected(self):
        return not self.resistance


def build_network(matrix):
    computers = [Node(i, matrix[i][i]) for i in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] and i != j:
                computers[i].add_link(computers[j])
    return computers

def capture(matrix):
    network = build_network(matrix)

    time = 0
    infected_computers = set()
    infected_computers.add(network[0])
    while not all(pc.is_infected for pc in network):
        for computer in infected_computers:
            computer.attack()
        time += 1
        infected_computers.update([computer for computer in network if computer.is_infected])
    return time

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"