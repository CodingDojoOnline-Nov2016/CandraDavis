# You're going to create a program that simulates tossing a coin 5,000 times. Your program should display how many times the head/tail appears.
def create_random_numbers():
    toss_list = []
    i = 1
    while i <= 5000:
        import random
        random_num = random.random()
        toss_list.append(random_num)
    i +=1
    # return toss_list
print create_random_numbers()

# heads_tails_list = create_random_numbers()
# def coin_toss():
#     for num in heads_tails_list:
#         num.round
# print coin_toss()

        # print "Attempt #" + str(i) + ":  Throwing a coin...It's "


        # if random_num.round is 0:
        #     t = 'tails'
        # elif random_numb.round is 1:
        #     y = 'heads'
