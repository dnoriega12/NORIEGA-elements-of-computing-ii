from .warrior import Warrior

# Coding Challenge: Add Your Own Class
class Rogue(Warrior):
    # Initialize warrior attributes
    def __init__(self, name, level, health, strength, stealth):
        # Inherit attributes
        super().__init__(name, level, health, strength)
        
        # Initialize the Rogue's specific attribute: stealth
        self.stealth = stealth

    # Create sneak attack that targets and reduces health of another player
    def sneak_attack(self, target):

        # Reduce the target's health by a factor of stealth
        target.health -= self.stealth

        # Return a message describing the sneak attack action
        return f"{self.name} attacks {target.name}. Health has been reduced by {self.stealth} !"
