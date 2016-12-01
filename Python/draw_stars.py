# Create a function called  draw_stars() that takes a list of numbers and prints out  *.
# x = [4, 6, 1, 3, 5, 7, 25]
# def draw_stars(list):
#     for num in list:
#         print num * '*'
#
# draw_stars(x)

# Modify the function above. Allow a list containing integers and strings to be passed to the  draw_stars() function. When a string is passed, instead of  displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part.

x1 = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_stars1(list):
    for item in list:
        if type(item) is int:
            print item * '*'
        elif type(item) is str:
            first_initial = item[0].lower()
            print first_initial * len(item)
draw_stars1(x1)

#This second part was a bit more challenging. I need to get clear in mind what functions are available to me. i.e. type(), is int, is str, etc.
