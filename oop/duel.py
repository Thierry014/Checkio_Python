class Warrior():
    def __init__(self, health=50,attack=5):
        self.health = health
        self.attack = attack
        self.is_alive = True
    


class Knight(Warrior):
    def __init__(self):
        # call super() function to inhrenet from parent class
        super().__init__()
        self.attack = 7 


def fight (a,b):
    # check whether a,b is warrior object 
    while a.health > 0 and b.health > 0:
        b.health -= a.attack
        if b.health <= 0:
            b.is_alive = False
            return True
        a.health -= b.attack
        if a.health <= 0:
            a.is_alive = False
            return False


    # while a.health and b.health > 0:

    


chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()
print(fight(dave, carl))
print(fight(chuck, bruce))

print(chuck.is_alive)
# ! 
# 1. define the parent class include its property 
# 2. define children class use super() to inherent 