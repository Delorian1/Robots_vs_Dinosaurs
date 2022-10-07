from battlefield import Battlefield
import random

# As a developer, I want the battle to conclude once either 
# the robot or the dinosaur has its health points reduced to zero.

# Bonus Points:

# (5 points): As a developer, I want to choose from a List of 3 possible 
# weapons before a robot makes an attack.

# (5 points): As a developer, I want to create Fleet and Herd classes, 
# allowing for a list of 3 Robots to battle against a list of 3 Dinosaurs.

battlefild = Battlefield()
battlefield.run_game()


Mecha_Godzilla_weapons_list = ["proton_scream","plasma_punch", "rotating_buzzsaw"]
Godzilla_weapons_list = ["atomic beam", "Godzilla_breath", "Mothra_powerup"]
list_of_weapons = [Mecha_Godzilla_weapons_list, Godzilla_weapons_list ]

print("list_of_weapons")

Mecha_jaegers_list = ["Gypsy_Avenger","Saber_Athena","Bracer_Phoenix","Guarian_Bravo","Striker_Eureka","Cherno_Alpha","Crimson_Typhoon"