from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1,self.sides))


dice_6_sides = Die(6)
for i in range(10):
    dice_6_sides.roll_die()

dice_10_sides = Die(10)
for i in range(10):
    dice_10_sides.roll_die()


dice_20_sides = Die(20)
for i in range(20):
    dice_20_sides.roll_die()