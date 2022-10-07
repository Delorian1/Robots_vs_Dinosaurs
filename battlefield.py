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
        self.robot = robot("Mecha_Godzilla")
        self.dinosaur = dinosaur("Godzilla")
        
    def run_game(self):
        self.display_welcome()
    
    def display_welcome(self):
        print(f' Welcome to Mechanixx, where the future and the past collide')
    
    def battle_phase(self):
        pass

    def reduce_health(amount):
        self.health -= amount

    def fight():
        dinosaur_reduce_health(robot.calculate.damage())
        dinosaur.check_dead()
        robot_reduce_health(dinosaur.calculate.damage())
        robot.check_dead()

    def display_winner(self):
        pass
