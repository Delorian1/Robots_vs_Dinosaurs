from weapon import Weapon
#(10 points): As a developer, I want a Dinosaur to have a name, health, 
# and attack power.

class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.attack_power = 10
        self.health =  50

    def attack(self, robot):
        robot.health -= self.attack
        print(f'{robot.name} was attacked by {self.name} and did {self.attack_power} damage.')
      
    
        
    
