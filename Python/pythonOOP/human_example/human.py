import random
class Human(object):
    """docstring for Human."""
    def __init__(self, clan=None):
# Python's protocol methods -- the magic methods whose names start and end with double underscores
        print 'New Human!!!'
        self.health = 100
        self.clan = clan
        self.strength = 3
        self.stealth = 3
        self.intelligence = 3
# For any blueprint(class), we're going to need to describe whatever it is we are making a blueprint for. One way we could describe the object/thing is by defining what it can do. Enter methods.
    def taunts(self):
        print 'You want a piece of me?'
# methods are functions that describe what my object/instance can do. This method below means my human(candra) has the ability to attack(i.e. run the attacks function).
    def attacks(self):
        self.taunt()
        luck = round(random.random() * 100)
        if(luck > 50):
            if((luck * stealth) > 150 ):
                print 'attacking'
                return True
            else:
                print 'attack failed'
                return False
        else:
            self.health -= self.strength
            print 'attack failed'
            return False


candra = Human()
print candra   # Basically, the output gives you information about what class your object belongs to and where it is stored in memory.  *** this instantiates the object (creates an instance / creates an object)***
candra.taunts() #this invokes the method of taunt
Ric = Human()
print Ric

#
# Debugging a Class Definition
# When we get syntax errors on a class definition, it can be in the class line or one of the internal method function definitions.
#
    # If we get a simple SyntaxError on the first line, we have misspelled class, left off an ( or ), or ommitted the ':' that begins the suite of statements that defines the class.
    #
    # If we get a syntax error further in the class definition, then our method functions are not defined correctly. Be sure to indent the def once ( so it nexts inside the class). Be sure to indent the suite of statments inside the def twice.

# Debugging Object Construction
# Assuming we have defined the class correctly, there are three things that can go wrong when attempting to construct an ojbect of that class.
#
    # The class name is spelled incorrectly.
    # You have omitted the () after the class name. If we say my_object= MyClass, we have assigned the class object, MyClass, to the variable my_object. We have to say my_object= MyClass() to use the class name as a factory and create an instance of a class.
    # You have got incorrect argument values for the parameters of the __init__().

# Debugging Class vs. Object Issues
    # Perhaps the biggest mistake newbies make is attempting to exercise the method functions of a class instead of a specific object. You can not easily say  MyClass.my_function(), you will get the cryptic TypeError: unbound method error message. The phrase "unbound method" means that no instance was being used.
    #
    # When you say  x= MyClass(), you are creating an instance. When you see x.my_function(), then you are asking that specific object to do its my_function() operation.
