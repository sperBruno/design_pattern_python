from abc import ABCMeta, abstractmethod


class Beverage(metaclass=ABCMeta):
    description = "Unknown beverage"


    def get_description(self):
        return self.description

    def cost(self):
        pass
