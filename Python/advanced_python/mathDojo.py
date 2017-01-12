# PART I
# Create a Python class called MathDojo that has the methods  add and subtract. Have these 2 functions take at least 1 parameter.
#
# Then create a new instance called md. It should be able to do the following task:
# MathDojo().add(2).add(2, 5).subtract(3, 2).result
# which should perform 0+2+(2+5)-(3+2) and return 4.
import math

class MathDojo(object):
    """docstring for MathDojo."""
    def __init__(self, val = None):
        self.val = val
        self.sum = 0
        self.minus = 0
    def add_num(self, num1, *restOfNums):
        self.num1 = num1
        num_list = []
        for each_num in restOfNums:
            num_list.append(each_num)
        num_list.append(self.num1)
        add_all = sum(num_list)
        self.sum += add_all
        print str(self.sum)
        return self
    def subtract_num(self, num1, *restOfNums):
        self.num1 = num1
        num_list = []
        for each_num in restOfNums:
            num_list.append(each_num)
        num_list.append(self.num1)
        subtract_all = sum(num_list) * -1
        self.minus += subtract_all
        print str(self.minus)
        return self
    def result(self):
        result = self.sum + self.minus
        print str(result)
        return self

md = MathDojo()
md.add_num(2).add_num(2,5).subtract_num(3,2).result()
