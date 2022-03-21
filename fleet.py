from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self, robo_1, robo_2, robo_3):
        self.robots.append(robo_1)
        self.robots.append(robo_2)
        self.robots.append(robo_3)
        print(f"The current fleet consists of {robo_1.name} ({robo_1.health} HP), {robo_2.name} ({robo_2.health} HP), and {robo_3.name} ({robo_3.health} HP.)")