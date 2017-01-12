# Objective
# The objective of this assignment is to help you understand inheritance. Remember that a class is more than just a collection of properties and methods. If you want to create a new class with attributes and methods that are already defined in another class, you can have this new class inherit from that other class (called the parent) instead of copying and pasting code from the original class. Child classes can access all the attributes and methods of a parent class AND have new attributes and methods of its own, for child instances to call. As we see with Wizard / Ninja / Samurai (that are each descended from Human), we can have numerous unique child classes that inherit from the same parent class.
#
# To Do
# Create a class called Animal with the following attributes: name, and health. Give the animal following three methods: walk, run, and displayHealth. Give a new animal a health of 100 when it gets created. When a walk() method is invoked, have the health decrease by 1. When a run() method is invoked, have the health decrease by 5. When a displayHealth() method is invoked, display on screen the name of the Animal and the health.
#
# Create an instance of the animal called 'animal' and have this animal walk three times, run twice, and have it display its health.
#
# Now for the first instance of the animal (instance called 'animal'), try calling fly() or pet() and make sure this doesn't work.  (-:
class Animal(object):
    """docstring for Animal."""
    def __init__(self, name):
        self.name = name
        self.health = 100
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print 'Name: ' + str(self.name)
        print 'Health: ' + str(self.health)
        return self

animal = Animal('Jeff')
animal.walk().walk().walk().run().run().displayHealth()
