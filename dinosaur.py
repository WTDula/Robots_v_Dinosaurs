class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 10
        self.attack_power = attack_power
        self.attack_name = ""
        self.energy = 20

    def attack(self, robo):
        if(robo.health > 0):
            self.choose_attack() # when attack runs, have dinosaur choose what attack to use for the turn
            print(f"{self.name} attacks {robo.name} with {self.attack_name} ({self.attack_power} damage!)") # display message
            robo.health -= self.attack_power
            self.energy -= 10
            if(robo.health < 0): # if attack brings robo's health below zero
                robo.health = 0  # make robo's health zero
        else:
            print(f"{self.name} attacked a lump of metal! Way to waste a turn!") # if attacking a robo with zero health, display message and move on
    
    def choose_attack(self):
        attack_tuple = ("Bite", "Scratch", "Tail Whip")
        for attack in attack_tuple:
            print(f"\t {attack}")
        user_input = input("Choose your attack: (1, 2, 3) ")
        if(user_input == "1"):
            self.attack_name = attack_tuple[0]
        elif(user_input == "2"):
            self.attack_name = attack_tuple[1]
        else:
            self.attack_name = attack_tuple[2]
