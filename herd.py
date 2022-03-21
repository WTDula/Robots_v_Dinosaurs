from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self, dino_1, dino_2, dino_3):
        self.dinosaurs.append(dino_1)
        self.dinosaurs.append(dino_2)
        self.dinosaurs.append(dino_3)
        print(f"The current herd consists of {dino_1.name} ({dino_1.health} HP), {dino_2.name} ({dino_2.health} HP), and {dino_3.name} ({dino_3.health} HP.)")