# You're going to create a program that simulates tossing a coin 5,000 times. Your program should display how many times the head/tail appears.
def create_random_numbers():
    toss_list = []
    for count in range(0, 5):
        import random
        random_num = random.random()
        round(random_num)
        toss_list.append(random_num)
    return toss_list

heads_tails_list = create_random_numbers()

# print heads_tails_list
def coin_toss():
    count = 1
    for num in heads_tails_list:
        if num == 1:
            print "Attempt #" + str(count) + ":  Throwing a coin...It's heads"
        else:
            print "Attempt #" + str(count) + ":  Throwing a coin...It's tails"
        count +=1
print coin_toss()
        # print "Attempt #" + str(i) + ":  Throwing a coin...It's "


        # if random_num.round is 0:
        #     t = 'tails'
        # elif random_numb.round is 1:
        #     y = 'heads'
