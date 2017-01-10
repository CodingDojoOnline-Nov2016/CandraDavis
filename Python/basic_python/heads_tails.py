# You're going to create a program that simulates tossing a coin 5,000 times. Your program should display how many times the head/tail appears.
def coin_toss():
    import random
    import math
    count_heads = 0
    count_tails = 0
    for count in range(0, 5001):
        random_num = round(random.random())
        if random_num == 1:
            side = 'head'
            count_heads += 1
        else:
            side = 'tail'
            count_tails += 1

        print "Attempt #" + str(count) + ":  Throwing a coin...It's a " + side + "!...Got " + str(count_heads) + " head(s) so far and " + str(count_tails) + " tail(s) so far"
print coin_toss()
        # print "Attempt #" + str(i) + ":  Throwing a coin...It's "


        # if random_num.round is 0:
        #     t = 'tails'
        # elif random_numb.round is 1:
        #     y = 'heads'
