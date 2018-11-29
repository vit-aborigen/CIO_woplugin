from collections import defaultdict

class Friends:
    def __init__(self, connections):
        self.connections = defaultdict(lambda: set())
        for friend_1, friend_2 in connections:
            self.connections[friend_1] |= {friend_2}
            self.connections[friend_2] |= {friend_1}

    def add(self, connection):
        friend_1, friend_2 = connection
        if friend_2 in self.connections.get(friend_1, []):
            return False
        self.connections[friend_1] |= {friend_2}
        self.connections[friend_2] |= {friend_1}
        return True

    def remove(self, connection):
        friend_1, friend_2 = connection
        if friend_2 not in self.connections.get(friend_1, []):
            return False
        self.connections[friend_1] ^= {friend_2}
        self.connections[friend_2] ^= {friend_1}
        return True

    def names(self):
        return set([k for k,v in self.connections.items() if len(v)])

    def connected(self, name):
        return self.connections[name]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
