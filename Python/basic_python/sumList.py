# Create a program that prints the sum of all the values in the list:

a = [1, 2, 5, 10, 255, 3]
sum(i in i for a)
# this works because the sum function adds the numbers progressively as the for loop travels through the list.

#
# def sumList(list):
#     for i in range(6, 0, -1):
#         add1 = a[len(a)-1]
#         sumNum = add1 + a[len(a) -2]
#
# sumList(a)
#This doesn't work because it only adds adjacent numbers, not each number progressively.
#
# def sumList(list):
#     for num in range(list):
#         sumNum = sum(a[num])
#     return list
#
# print sumList(a)
# this logic doesn't work because I couldn't figure out how to add numbers progressively without just adding adjacent numbers. Same problem as above
