import random


class Dice:
    def roll(self):
        firsrt = random.randint(1,6)
        second = random.randint(1,6)
        return firsrt, second


dice = Dice()
print(dice.roll())
