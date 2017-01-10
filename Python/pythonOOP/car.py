# Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%.
#
# Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.
#
# A sample output would be like this:
#
# Price: 2000
# Speed: 35mph
# Fuel: Full
# Mileage: 15mpg
# Tax: 0.12
class Car(object):
    """docstring for Car."""
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12
    def display_all(self):
        print 'Price: ' + str(self.price)
        print 'Speed: ' + str(self.speed) + 'mph'
        print 'Fuel: ' + str(self.fuel)
        print 'Mileage: ' + str(self.mileage) + 'mpg'
        print 'Tax: ' + str(self.tax)

car1 = Car(3000, 125, "half", 7)
car1.display_all()
car2 = Car(2000, 25, "full", 25)
car2.display_all()
car3 = Car(10000, 75, "quarter", 34)
car3.display_all()
car4 = Car(45000, 125, "half", 22)
car4.display_all()
car5 = Car(9000, 125, "half", 6)
car5.display_all()
car6 = Car(15000, 12, "full", 45)
car6.display_all()
