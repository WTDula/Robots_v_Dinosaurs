from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()

    def run_game(self):
        self.display_welcome()
        self.herd.create_herd()
        self.fleet.create_fleet()
        self.battle()

    def display_welcome(self):
        print("Welcome to Robots Versus Dinosaurs!  Who will be the winner?")
        print("-------------------------------------------------------------------")

    def battle(self):
        dino_total_health = self.calc_total_dino_health()
        robo_total_health = self.calc_total_robot_health()
        while(dino_total_health > 0 and robo_total_health > 0):
            self.display_dinosaurs()
            user_input = input("Which dinosaur would you like to attack with? (1, 2, 3) ")
            if(user_input == "1"):
                self.dino_turn(self.herd.dinosaurs[0])
            elif(user_input == "2"):
                self.dino_turn(self.herd.dinosaurs[1])
            else:
                self.dino_turn(self.herd.dinosaurs[2])
            if(self.calc_total_robot_health() == 0):    # if attack causes total robot health to hit zero,
                break                                   # break out of loop to display winners
            self.display_robots()
            user_input = input("Which robot would you like to attack with? (1, 2, 3) ")
            if(user_input == "1"):
                self.robo_turn(self.fleet.robots[0])
            elif(user_input == "2"):
                self.robo_turn(self.fleet.robots[1])
            else:
                self.robo_turn(self.fleet.robots[2])
            dino_total_health = self.calc_total_dino_health()
            robo_total_health = self.calc_total_robot_health()
        self.display_winners()


    def dino_turn(self, dino):
        if(dino.health == 0):
            print("That dinosaur is dead, no necromancy!")  # if selected dino's health = 0
            return                                          # skip turn
        if(dino.energy == 0):
            print("That dinosaur has no energy!")           # if selected dino's energy = 0
            return                                          # skip turn
        self.show_dino_opponent_options()
        user_input = input("Which enemy do you wish to attack? (1, 2, 3) ")
        if(user_input == "1"):
            dino.attack(self.fleet.robots[0])
        elif(user_input == "2"):
            dino.attack(self.fleet.robots[1])
        else:
            dino.attack(self.fleet.robots[2])

    def robo_turn(self, robo):
        if(robo.health == 0):
            print("That robot has been terminated!")        # if selected robo's health = 0
            return                                          # skip turn
        if(robo.power_level == 0):
            print("That robot has no remaining power!")     # if selected robo's power_level = 0
            return                                          # skip turn
        self.show_robo_opponent_options()
        user_input = input("Which enemy would you lke to attack? (1, 2, 3) ")
        if(user_input == "1"):
            robo.attack(self.herd.dinosaurs[0])
        elif(user_input == "2"):
            robo.attack(self.herd.dinosaurs[1])
        else:
            robo.attack(self.herd.dinosaurs[2])

    # I am the dino, show me the robos I can attack
    def show_dino_opponent_options(self):
        self.display_robots()


    # I am the robo, show me the dinos I can attack
    def show_robo_opponent_options(self):
        self.display_dinosaurs()

    # display winners based on total health (compare robot health since dinos went first)
    def display_winners(self):
        self.display_dinosaurs()
        self.display_robots()
        if(self.calc_total_robot_health() == 0):
            print("Dinosaurs win!")
        else:
            print("Robots win!")

    # repetitive display put in own function
    def display_dinosaurs(self):
        print("-----------------------------------------------------------------------------")
        print(f" 1. {self.herd.dinosaurs[0].name}'s HP = {self.herd.dinosaurs[0].health} ")
        print(f" 2. {self.herd.dinosaurs[1].name}'s HP = {self.herd.dinosaurs[1].health} ")
        print(f" 3. {self.herd.dinosaurs[2].name}'s HP = {self.herd.dinosaurs[2].health} ")

    # repetitive display put in own function
    def display_robots(self):
        print("-----------------------------------------------------------------------------")
        print(f" 1. {self.fleet.robots[0].name}'s HP = {self.fleet.robots[0].health} ")
        print(f" 2. {self.fleet.robots[1].name}'s HP = {self.fleet.robots[1].health} ")
        print(f" 3. {self.fleet.robots[2].name}'s HP = {self.fleet.robots[2].health} ")

    # repetitive calculation
    def calc_total_dino_health(self):
        return self.herd.dinosaurs[0].health + self.herd.dinosaurs[1].health + self.herd.dinosaurs[2].health

    # repetitive calculation
    def calc_total_robot_health(self):
        return self.fleet.robots[0].health + self.fleet.robots[1].health + self.fleet.robots[2].health