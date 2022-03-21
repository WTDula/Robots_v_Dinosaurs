class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 10
        self.attack_power = attack_power

    def attack(self, robo):
        if(robo.health > 0):
            print(f"{self.name} attacks {robo.name} ({self.attack_power} damage!)")
            robo.health -= self.attack_power
            if(robo.health < 0):
                robo.health = 0
        else:
            print(f"{self.name} attacked a lump of metal! Way to waste a turn!")