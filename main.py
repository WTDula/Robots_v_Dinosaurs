from battlefield import Battlefield
from robot import Robot
from dinosaur import Dinosaur

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