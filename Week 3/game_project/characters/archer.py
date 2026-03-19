from .warrior import Warrior

class Archer(Warrior):
    def __init__(self, name, level, health, strength, arrows):
        super().__init__(name, level, health, strength)
        self.arrows = arrows

    def fire_arrow(self, target):
        if self.arrows > 0:
            self.arrows -= 1
            target.health -= self.strength
            return f"{self.name} fires an arrow at {target.name} for {self.strength} damage!"
        else:
            return f"{self.name} has no arrows left!"