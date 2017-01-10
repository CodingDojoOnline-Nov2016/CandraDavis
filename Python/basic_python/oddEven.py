# Create a function that counts from 1 to 2000. As it loops through each number, have your program generate the number and specify whether it's an odd or even number.
# def num0to2000():
# number = num0to2000()
# originally tried to create a function that ran the for loop and then use the values of that function to add to my oddEven function. This was TOTALLY unnecessary.

def oddEven():
    for num in range(0, 2001, 1):
        if num % 2 == 0:
            print "Numer is " + str(num) + ".  This is an even number."
        else:
            print "Number is " + str(num) + ".  This is an odd number."

oddEven()
