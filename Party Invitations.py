class Observer:
    def __init__(self):
        self.data = None

    def notify(self, *args):
        self.data = args[0]


class Observable:
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self, *args):
        for observer in self.observers:
            observer.notify(args)


class Friend(Observer):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def show_invite(self):
        if not self.data:
            return 'No party...'
        place, time = self.data
        return '{}: {}'.format(place, time)

class Party(Observable):
    def __init__(self, place):
        super().__init__()
        self.place = place

    def add_friend(self, person):
        super(Party, self).register_observer(person)

    def del_friend(self, person):
        super(Party, self).remove_observer(person)

    def send_invites(self, time):
        super(Party, self).notify_observers(self.place, time)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    party = Party("Midnight Pub")
    nick = Friend("Nick")
    john = Friend("John")
    lucy = Friend("Lucy")
    chuck = Friend("Chuck")

    party.add_friend(nick)
    party.add_friend(john)
    party.add_friend(lucy)
    party.send_invites("Friday, 9:00 PM")
    party.del_friend(nick)
    party.send_invites("Saturday, 10:00 AM")
    party.add_friend(chuck)

    print(john.show_invite())

    assert john.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert nick.show_invite() == "Midnight Pub: Friday, 9:00 PM"
    assert chuck.show_invite() == "No party..."
    print("Coding complete? Let's try tests!")