from human import Human

class Wizard(Human):
    # """docstring for Wizard."""
    def __init__(self):
        super(Wizard, self).__init__()  #use super to call the Human __init__ method. Has all the attributes of Human
        self.intelligence = 10          #every wizard starts off with greater intelligence than Human
    def heal(self):
        self.health += 10

class Ninja(Human):
    # """docstring for Ninja."""
    def __init__(self, arg):
        super(Ninja, self).__init__()
        self.stealth = 10
    def steal(self):
        self.stealth += 5

class Samurai(Human):
    # """docstring for Samurai."""
    def __init__(self, arg):
        super(Samurai, self).__init__()
        self.strength = 10
    def sacrifice(self):
        self.health -= 5

harry = Wizard()
rain = Ninja()
matt = Samurai()

harry.heal()
print harry.health

rain.steal()
print rain.stealth

matt.sacrifice()
print matt.health
print matt.stealth
