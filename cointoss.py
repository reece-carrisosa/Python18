def coin_toss():
    import random
    head_count = 0
    tail_count = 0
    
    for x in range(1,5001):
        random_num = random.random()
        random_num = round(random_num)
        print random_num
        if random_num == 1:
            head_count += 1
            print "Attempt #", x, ": Throwing a coin... It's a head! ... Got", head_count, "head(s) so far and", tail_count, "tail(s) so far"
        
        else:
            tail_count += 1
            print "Attempt #", x, ": Throwing a coin... It's a tail! ... Got", head_count, "head(s) so far and", tail_count, "tail(s) so far"

coin_toss()




# import random

# def toss(reps):
#     # print new_toss
#     attempt_count = 1
#     head_count = 0
#     tail_count = 0
#     result = ""
#     result_string_complete = ""

#     for x in range(1, reps):
#         new_toss = random.randint(0,1)
#         if new_toss == 1:
#             head_count += 1
#             result = "head"
#             print "Attempt #", attempt_count, ": Throwing a coin... It's a ", result, "! Got ", head_count, "head(s) so far and", tail_count, "tail(s) so far"
#         else:
#             tail_count += 1
#             result = "tail"
#             print "Attempt #", attempt_count, ": Throwing a coin... It's a ", result, "! Got ", head_count, "head(s) so far and", tail_count, "tail(s) so far"
#         attempt_count += 1

# toss(5001)