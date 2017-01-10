# Create a new class called Bike with the following properties/attributes:
#
# price
# max_speed
# miles
# Create 3 instances of the Bike class.
#
# Use the __init__() function to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); In the __init__() also write the code so that the initial miles is set to be 0 whenever a new instance is created.
#
# Add the following functions to this class:
#
# displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
# ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
# reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
# Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().
#
# What would you do to prevent the instance from having negative miles?
class Bike(object):
    """docstring for bike."""
    def __init__(self, price, max_speed):
        self.miles = 0
        self.price = price
        self.max_speed = max_speed
    def displayInfo(self):
        print 'Price is: $' + str(self.price)
        print 'Max speed is: ' + str(self.max_speed) + 'mph'
        print 'Total miles are: ' + str(self.miles)
        return self
    def ride(self):
        print 'Riding'
        self.miles += 10
        return self
    def reverse(self):
        print 'Reversing'
        if self.miles >= 5:
            self.miles -= 5
        else:
            print 'Can not ride backwards!'
        return self

bike1 = Bike(200, 5)
bike1.ride().ride().ride().displayInfo()
# bike1.ride()
# bike1.ride()
# bike1.displayInfo()
bike2 = Bike(150, 3)
bike2.ride().ride().reverse().reverse().displayInfo()
# bike2.ride()
# bike2.reverse()
# bike2.reverse()
# bike2.displayInfo()
bike3 = Bike(75, 1)
bike3.reverse().reverse().reverse().displayInfo()
# bike3.reverse()
# bike3.reverse()
# bike3.displayInfo()
