from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()

    def run_game(self):
        self.herd.create_herd()
        self.fleet.create_fleet()
        self.battle()

    def display_welcome(self):
        print("Welcome to Robots Versus Dinosaurs!  Who will be the winner?")
        print("-------------------------------------------------------------------")

    def battle(self):
        dino_total_health = self.calc_total_dino_health()
        robo_total_health = self.calc_total_robot_health()
        while(dino_total_health > 0 or robo_total_health > 0):
            self.display_dinosaurs()
            user_input = input("Which dinosaur would you like to attack with? (1, 2, 3) ")
            if(user_input == 1):
                self.dino_turn(self.herd.dinosaurs[0])
            elif(user_input == 2):
                self.dino_turn(self.herd.dinosaurs[1])
            else:
                self.dino_turn(self.herd.dinosaurs[2])
            self.display_robots()
            user_input = input("Which robot would you like to attack with? (1, 2, 3) ")
            if(user_input == 1):
                self.robo_turn(self.fleet.robots[0])
            elif(user_input == 2):
                self.robo_turn(self.fleet.robots[1])
            else:
                self.robo_turn(self.fleet.robots[2])
            dino_total_health = self.calc_total_dino_health()
            robo_total_health = self.calc_total_robot_health()
        self.display_winners()


    def dino_turn(self, dino):
        self.show_dino_opponent_options()
        user_input = input("Which enemy do you wish to attack? (1, 2, 3) ")
        if(user_input == 1):
            dino.attack(self.fleet.robots[0])
        elif(user_input == 2):
            dino.attack(self.fleet.robots[1])
        else:
            dino.attack(self.fleet.robots[2])

    def robo_turn(self, robo):
        self.show_robo_opponent_options()
        user_input = input("Which enemy would you lke to attack? (1, 2, 3) ")
        if(user_input == 1):
            robo.attack(self.herd.dinosaurs[0])
        elif(user_input == 2):
            robo.attack(self.herd.dinosaurs[1])
        else:
            robo.attack(self.herd.dinosaurs[2])

    # I am the dino, show me the robos I can attack
    def show_dino_opponent_options(self):
        self.display_robots()


    # I am the robo, show me the dinos I can attack
    def show_robo_opponent_options(self):
        self.display_dinosaurs()


    def display_winners(self):
        pass

    def display_dinosaurs(self):
        print(f" 1. {self.herd.dinosaurs[0].name}'s HP = {self.herd.dinosaurs[0].health} ")
        print(f" 2. {self.herd.dinosaurs[1].name}'s HP = {self.herd.dinosaurs[1].health} ")
        print(f" 3. {self.herd.dinosaurs[2].name}'s HP = {self.herd.dinosaurs[2].health} ")
        print("-----------------------------------------------------------------------------")

    def display_robots(self):
        print(f" 1. {self.fleet.robots[0].name}'s HP = {self.fleet.robots[0].health} ")
        print(f" 2. {self.fleet.robots[1].name}'s HP = {self.fleet.robots[1].health} ")
        print(f" 3. {self.fleet.robots[2].name}'s HP = {self.fleet.robots[2].health} ")
        print("-----------------------------------------------------------------------------")

    def calc_total_dino_health(self):
        return self.herd.dinosaurs[0].health + self.herd.dinosaurs[1].health + self.herd.dinosaurs[2].health

    def calc_total_robot_health(self):
        return self.fleet.robots[0].health + self.fleet.robots[1].health + self.fleet.robots[2].health