class Text:
    def __init__(self):
        self.text = ''
        self.font = None

    def write(self, text):
        self.text += text

    def set_font(self, font):
        self.font = font

    def show(self):
        return '[{0}]{1}[{0}]'.format(self.font, self.text) if self.font else self.text

    def restore(self, data):
        self.font = data[0]
        self.text = data[1]


class SavedText:
    def __init__(self):
        self.version = -1
        self.state = {}

    def save_text(self, text):
        self.version += 1
        self.state[self.version] = (text.font, text.text)

    def get_version(self, number):
        if number in self.state:
            return self.state[number]


if __name__ == '__main__':
    text = Text()
    saver = SavedText()

    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"

    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "

    print("Coding complete? Let's try tests!")