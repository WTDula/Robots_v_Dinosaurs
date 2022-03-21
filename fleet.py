from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        arnold = Robot("Terminator")
        bender = Robot("Bender")
        halo = Robot("Guilty Spark")
        self.robots.append(arnold)
        self.robots.append(bender)
        self.robots.append(halo)
        print(f"The current fleet consists of {arnold.name} ({arnold.health} HP), {bender.name} ({bender.health} HP), and {halo.name} ({halo.health} HP.)")