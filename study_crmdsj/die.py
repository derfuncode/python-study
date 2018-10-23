from random import randint

class Die():
    def __init__(self,sides = 6):
        self.sides = sides
    
    def roll_die(self):
        x = randint(1,self.sides)
        print(str(self.sides)+" sides roll die is "+ str(x))
    

my6die = Die()

for i in range(10):
    my6die.roll_die()

my10die = Die(10)
for i in range(10):
    my10die.roll_die()

    


