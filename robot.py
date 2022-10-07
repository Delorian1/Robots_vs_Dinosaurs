from weapon import Weapon
# As a developer, I want a Robot to have a name,health, and active_weapon.

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.active_weapon = Weapon("sword")

    def attack(self, dinosaur):
        self.dinosaur = dinosaur
        dinosaur.health -= self.weapon.attack_power
        print(f'{dinosaur.name} was attacked by {self.name}and did {self.attack_power} damage.')
      
        