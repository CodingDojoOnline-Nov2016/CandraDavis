# Create a function called 'multiply' that reads each value in the list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
a = [2, 4, 10, 16]
def multiply(list, val):
    multipleList = [i * val for i in list]
    return multipleList

b = multiply(a, 5)
print b
