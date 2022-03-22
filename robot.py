from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.weapon = Weapon("laser", 50)


    def attack(self, dino):
        if(dino.health > 0):
            self.choose_weapon()
            print(f"{self.name} attacks {dino.name} with {self.weapon.name} ({self.weapon.attack_power} damage!)") # display message
            dino.health -= self.weapon.attack_power
            if(dino.health < 0): # if attack brings dino's health to below zero,
                dino.health = 0  # make health zero
        else:
            print(f"{self.name} attacked a corpse! What a waste of a turn!") # if attacking a dino w/ zero health, display message and move on

    def choose_weapon(self):
        weapon_list = [Weapon("Laser", 50), Weapon("Kiss my shiny metal ass!", 100), Weapon("Lever-action shotgun", 75)] # list of weapon objects to choose from
        for gun in weapon_list:
            print(f"\t{gun.name}") # display guns
        user_input = input("Choose your weapon: (1, 2, 3) ")
        if(user_input == "3"):
            self.weapon = weapon_list[2] # assign chosen weapon as self.weapon
        elif(user_input == "2"):
            self.weapon = weapon_list[1] # assign chosen weapon as self.weapon
        else:
            self.weapon = weapon_list[0] # default weapon = laser