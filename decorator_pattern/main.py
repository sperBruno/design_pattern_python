from decorator_pattern.espresso import Espresso
from decorator_pattern.mocha import Mocha
from decorator_pattern.whip import Whip

beverage2 = Espresso()
beverage2 = Mocha(beverage2)
beverage2 = Mocha(beverage2)
beverage2 = Whip(beverage2)
print(beverage2.get_description() + "$ " + str(beverage2.cost()))
