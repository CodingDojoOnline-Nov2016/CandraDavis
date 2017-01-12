# Now, create another class called Dog that inherits everything that the Animal does and has, but 1) have the default health be 150 and 2) add a new method called pet, which when invoked, increase the health by 5. Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth().
#
# Now, create another class called Dragon that also inherits everything from Animal, but 1) have the default health be 170 and 2) add a new method called fly, which when invoked, decreased the health by 10. Have the Dragon walk() three times, run() twice, fly() twice, and have it displayHealth(). When the Dragon's displayHealth function is called, have it say 'this is a dragon!' before it displays the default information (by calling the parent's displayHealth function).
from animal import Animal
class Dog(Animal):
    """docstring for Dog."""
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    """docstring for Dragon."""
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self

dog = Dog('Doug')
dog.walk().walk().walk().run().run().pet().displayHealth()
dragon = Dragon('Pete')
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()
