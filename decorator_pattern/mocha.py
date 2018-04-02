from decorator_pattern.condiment_decorator import CondimentDecorator


class Mocha(CondimentDecorator):

    def __init__(self, beverage):
        super().__init__()
        self.__beverage = beverage

    def get_description(self):
        return self.__beverage.get_description() + ", Mocha"

    def cost(self):
        return self.__beverage.cost() + 0.20