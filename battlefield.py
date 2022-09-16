from dinosaur import Dinosaur
from robot import Robot
# As a developer, I want a Dinosaur to have the ability to 
# attack a Robot on a Battlefield. This attack method should lower a 
# Robot’s health by the value of the Dinosaur’s attack_power.

# (10 points): As a developer, I want a Robot to have the ability to attack 
# a Dinosaur on a Battlefield. 
# 
# This attack method should lower the Dinosaur’s 
# health by the attack_power of the Robot’s active_weapon.


class Battlefield:
    def __init__(self):
        self.robot = "Mecha_Godzilla"
        self.dinosaur = "Godzilla"
        
    def run_game(self):
        pass
    
    def display_welcome(self):
        print("Mecha Quest")
    
    def battle_phase(self):
        pass

    def display_winner(self):
        pass
