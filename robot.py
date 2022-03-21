from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("laser", 50)


    def attack(self, dino):
        if(dino.health > 0):
            print(f"{self.name} attacks {dino.name} with {self.weapon.name} ({self.weapon.attack_power} damage!)")
            dino.health -= self.weapon.attack_power
            if(dino.health < 0):
                dino.health = 0
        else:
            print(f"{self.name} attacked a corpse! What a waste of a turn!")
