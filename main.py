from battlefield import Battlefield
from robot import Robot
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd

battlefield_1 = Battlefield()

arnold = Robot("Terminator")
bender = Robot("Bender")
halo = Robot("Guilty Spark")

t_rex = Dinosaur("T-Rex", 30)
raptor = Dinosaur("Velociraptor", 25)
triceratops = Dinosaur("Triceratops", 10)

#test robot attack
arnold.attack(t_rex)

#test dinosaur attack
raptor.attack(bender)

#test create_fleet
robo_fleet = Fleet()
robo_fleet.create_fleet(arnold, bender, halo)

#test ceate_herd
dino_herd = Herd()
dino_herd.create_herd(t_rex, raptor, triceratops)