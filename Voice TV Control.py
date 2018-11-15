class VoiceCommand:
    def __init__(self, channels):
        self.channels = channels
        self.position = 0
        self.amount = len(channels)

    def first_channel(self):
        self.position = 0
        return self.channels[self.position]

    def last_channel(self):
        self.position = -1
        return self.channels[self.position]

    def next_channel(self):
        self.position += 1
        return self.channels[self.position % self.amount]

    def previous_channel(self):
        self.position -= 1
        return self.channels[self.position % self.amount]

    def turn_channel(self, number):
        self.position = number - 1
        return self.channels[self.position]

    def current_channel(self):
        return self.channels[self.position % self.amount]

    def is_exist(self, value):
        if isinstance(value, int):
            result = value < self.amount
        else:
            result = value in self.channels
        return ('Yes' if result else 'No')



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    CHANNELS = ["BBC", "Discovery", "TV1000"]

    controller = VoiceCommand(CHANNELS)

    assert controller.first_channel() == "BBC"
    assert controller.last_channel() == "TV1000"
    assert controller.turn_channel(1) == "BBC"
    assert controller.next_channel() == "Discovery"
    assert controller.previous_channel() == "BBC"
    assert controller.current_channel() == "BBC"
    assert controller.is_exist(4) == "No"
    assert controller.is_exist("TV1000") == "Yes"
    print("Coding complete? Let's try tests!")