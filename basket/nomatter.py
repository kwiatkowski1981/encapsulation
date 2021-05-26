
class Fruit:
    def __init__(self, name: str, color: str, taste: str, fruit_type: str):
        self.name = name
        self.color = color
        self.taste = taste
        self.fruit_type = fruit_type


class Basket:
    def __init__(self):
        self.fruits = []
        self.quantity = len(self.fruits)

    def add_fruit(self, fruit: Fruit):
        self.fruits.append(fruit)
        self.quantity += 1
        return self.fruits

    def show_basket(self):
        print(f"ilosc produktow w koszyku: {self.quantity}\n")
        for fruit in self.fruits:
            print(f"{fruit.name} {fruit.fruit_type} {fruit.color} {fruit.taste}")
        print("\n")


class Report:
    def __init__(self, basket):
        self.basket = basket

    def get_for_color(self):
        report = {}
        for fruit in self.basket.fruits:
            if fruit.color not in report:
                report[fruit.color] = 0
            report[fruit.color] += 1
        return report

    def get_for_name(self):
        report = {}
        for fruit in self.basket.fruits:
            if fruit.name not in report:
                report[fruit.name] = 0
            report[fruit.name] += 1
        return report

    def get_for_fruit_type(self):
        report = {}
        for fruit in self.basket.fruits:
            if fruit.fruit_type not in report:
                report[fruit.fruit_type] = 0
            report[fruit.fruit_type] += 1
        return report

    def get_for_taste(self):
        report = {}
        for fruit in self.basket.fruits:
            if fruit.taste not in report:
                report[fruit.taste] = 0
            report[fruit.taste] += 1
        return report