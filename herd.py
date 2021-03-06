from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        t_rex = Dinosaur("T-Rex", 60)
        raptor = Dinosaur("Velociraptor", 55)
        triceratops = Dinosaur("Triceratops", 40)
        self.dinosaurs.append(t_rex)
        self.dinosaurs.append(raptor)
        self.dinosaurs.append(triceratops)
        print(f"The current herd consists of {t_rex.name} ({t_rex.health} HP), {raptor.name} ({raptor.health} HP), and {triceratops.name} ({triceratops.health} HP.)")