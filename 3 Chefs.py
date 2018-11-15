class AbstractCook:
    def __init__(self):
        self.food_total = 0
        self.drink_total = 0

    def add_food(self, amount, price):
        self.food_total += amount * price

    def add_drink(self, amount, price):
        self.drink_total += amount * price

    def total(self):
        return "{}: {}, {}: {}, Total: {}".format(self.food_name, self.food_total, self.drink_name,
                                                  self.drink_total, self.food_total + self.drink_total)

class JapaneseCook(AbstractCook):
    def __init__(self):
        super(JapaneseCook, self).__init__()
        self.food_name = 'Sushi'
        self.drink_name = 'Tea'

class RussianCook(AbstractCook):
    def __init__(self):
        super(RussianCook, self).__init__()
        self.food_name = 'Dumplings'
        self.drink_name = 'Compote'

class ItalianCook(AbstractCook):
    def __init__(self):
        super(ItalianCook, self).__init__()
        self.food_name = 'Pizza'
        self.drink_name = 'Juice'


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_food(3, 15)
    client_1.add_drink(2, 10)

    client_2 = RussianCook()
    client_2.add_food(1, 40)
    client_2.add_food(2, 25)
    client_2.add_drink(5, 20)

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_food(2, 30)
    client_3.add_drink(2, 10)

    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125"
    assert client_2.total() == "Dumplings: 90, Compote: 100, Total: 190"
    assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"
    print("Coding complete? Let's try tests!")