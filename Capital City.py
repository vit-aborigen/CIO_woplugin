class Singleton:
    instance = None
    def __new__(cls, *args):
        if not cls.instance:
            cls.instance = object.__new__(cls)
        return cls.instance

class Capital(Singleton):
    first_init = True

    def __init__(self, name):
        if self.first_init:
            self._name = name
            self.first_init = False

    def name(self):
        return self._name
