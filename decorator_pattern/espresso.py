from decorator_pattern.beverage import Beverage


class Espresso(Beverage):

    def __init__(self):

        self.description = "Espresso"

    def get_description(self):
        return self.description

    def cost(self):
        return 0.99