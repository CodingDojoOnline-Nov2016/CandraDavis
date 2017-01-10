# Create a program that prints the average of the values in the list:

a = [1, 2, 5, 10, 255, 3]
def averageList(list):
    sumList = sum(i for i in list)
    average = sumList / len(list)
    print average
    return

print averageList(a)
