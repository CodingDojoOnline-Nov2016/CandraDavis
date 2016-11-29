# Create a program that prompts the user ten times for a test score between 60 and 100. Each time a score is generated, your program should display what the grade is for a particular score. Here is the grade table:
#
# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A


def scoresGrades():
    for i in range(0, 10, 1):
        userScore = input('What is your score?')
        if userScore in range(0, 60):
            print "Score: " + str(userScore) + "; Your grade is F. You didn't study!"
        elif userScore in range(60, 70):
            print "Score: " + str(userScore) + "; Your grade is D."
        elif userScore in range(70, 80):
            print "Score: " + str(userScore) + "; Your grade is C."
        elif userScore in range(80, 90):
            print "Score: " + str(userScore) + "; Your grade is B."
        else:
            print "Score: " + str(userScore) + "; Your grade is A."
    else:
        print "End of program. Bye!"

scoresGrades()
        # return userScore
