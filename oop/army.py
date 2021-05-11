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

class Army():
    def __init__(self):
        self.team = []

    def add_units(self,warrior):
        self.team.append(warrior)



class Battle():
    def __int__(self):
        pass

    def fight(self,army1,army2):
        def fire(a,b):
    # check whether a,b is warrior object 
            while a.health > 0 and b.health > 0:
                b.health -= a.attack
                if b.health <= 0:
                    b.is_alive = False
                    return [True, a.health]
                a.health -= b.attack
                if a.health <= 0:
                    a.is_alive = False
                    return [False, b.health]


        # start fight 
        i,j = 0,0

        while i>-1:
            warrior1 = army1.team[i]
            warrior2 = army2.team[j]
            fight_result = fire(warrior1, warrior2)
            if fight_result[0]:
                # warrior1 win 
                print('1 win')
                warrior1.health = fight_result[1]
                j+= 1
                if j==len(army2.team):
                    return True
            else:
                #warrior2 win 
                (print('2 win'))
                army2.team[j].health = fight_result[1]
                i+= 1
                if i==len(army1.team):
                    return False



    

chuck = Warrior()
bruce = Warrior()
sam = Knight()
dave = Warrior()
mark = Warrior()

Team1 = Army()
Team1.add_units(chuck)
Team1.add_units(sam)

Team2 = Army()
Team2.add_units(dave)
Team2.add_units(mark)

battle = Battle()
print(battle.fight(Team1,Team2))