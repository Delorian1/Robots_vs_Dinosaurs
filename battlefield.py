from termios import VDISCARD
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
        self.battle_phase()   
    def display_welcome(self):
        print(f' Welcome to Deus ex Machina, where the monsters of future and past collide')
    
    def battle_phase(self):
        self.dinosaur.attack(self.robot)
        self.robot.attack(self.dinosaur)

    #calL THE attack function and set up a function to make them attack, robot 
    # add into a while loop

    # def reduce_health(amount):
    #     self.health -= amount

    # def fight():
    #     dinosaur_reduce_health(robot.calculate.damage())
    #     dinosaur.check_dead()
    #     robot_reduce_health(dinosaur.calculate.damage())
    #     robot.check_dead()

    def display_winner(self):
        pass
