VOWELS = "aeiouAEIOU"


class Chat:
    chat_history = []

    def __init__(self):
        self.human = None
        self.robot = None

    def store_message(self, user, message):
        Chat.chat_history.append((user, message), )

    def connect_human(self, human):
        self.human = human

    def connect_robot(self, robot):
        self.robot = robot

    def show_human_dialogue(self):
        msg = ""
        for person, message in Chat.chat_history:
            msg += "{} said: {}".format(person, message) + '\n'
        return msg[:-1]

    def show_robot_dialogue(self):
        msg = ""
        for person, message in Chat.chat_history:
            msg += "{} said: {}".format(person, ''.join(['0' if char in VOWELS else '1' for char in message])) + '\n'
        return msg[:-1]

class Human:
    def __init__(self, name):
        self.name = name

    def send(self, message):
        Chat.store_message(self, self.name, message)


class Robot:
    def __init__(self, SN):
        self.SN = SN

    def send(self, message):
        Chat.store_message(self, self.SN, message)

if __name__ == '__main__':
    chat = Chat()
    karl = Human('Karl')
    bot = Robot('R2D2')
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    chat.show_robot_dialogue()

