class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 10
        self.attack_power = attack_power

    def attack(self, robo):
        if(robo.health > 0):
            print(f"{self.name} attacks {robo.name} ({self.attack_power} damage!)") # display message
            robo.health -= self.attack_power
            if(robo.health < 0): # if attack brings robo's health below zero
                robo.health = 0  # make robo's health zero
        else:
            print(f"{self.name} attacked a lump of metal! Way to waste a turn!") # if attacking a robo with zero health, display message and move on