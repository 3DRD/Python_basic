import random


class Dice:
    def roll(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        result=(first,second)
        #return first,second | python interpretes it as Tuple
        print(result)


rolled=Dice()
rolled.roll()


