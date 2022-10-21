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
        self.robot = Robot("Mecha Godzilla")
        self.dinosaur = Dinosaur("Godzilla")
        
    def run_game(self):
        self.display_welcome()
        self.battle_phase()  

    def display_welcome(self):
        print(f'Welcome to Deus ex Machina, where the monsters of future and past collide!')
    
    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.dinosaur.attack(self.robot)
            if self.robot.health > 0:
               self.dinosaur.attack(self.robot) 
      
            
    def display_winner(self):                
        if self.dinosaur.health > 0:
            print("Godzilla WINS!")
        elif self.robot.self.health > 0:
            print("Mecha Godzilla WINS!")
       



 
   





    #calL THE attack function and set up a function to make them attack, robot 
    # add into a while loop

    # def reduce_health(amount):
    #     self.health -= amount

    # def fight():
    #     dinosaur_reduce_health(robot.calculate.damage())
    #     dinosaur.check_dead()
    #     robot_reduce_health(dinosaur.calculate.damage())
    #     robot.check_dead()

    
        
