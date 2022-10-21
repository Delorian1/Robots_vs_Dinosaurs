from weapon import Weapon
# As a developer, I want a Robot to have a name,health, and active_weapon.

class Robot:
    def __init__(self, name):
        self.name = ("Mecha Godzilla")
        self.health = 50
        self.attack_power = 10
        self.active_weapon = Weapon("sword")

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{dinosaur.name} was attacked by {self.name} and sustained {self.active_weapon.attack_power} damage.')
        print(f'{dinosaur.name} has {dinosaur.health} health remaining.')

        while self.robot.health > 0:
            continue

    
      
        