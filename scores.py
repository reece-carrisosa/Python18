def scores_grades():
    import random
    
    
    for x in range(1,11):
        random_num = random.randint(0,100)
        if random_num <= 60:
            print "Score:", random_num, "Your grade is F"

        elif random_num <=69:
            print "Score:", random_num, "Your grade is D"

        elif random_num <= 79:
            print "Score:", random_num, "Your grade is C"

        elif random_num <= 89:
            print "Score:", random_num, "Your grade is B"

        elif random_num <= 100:
            print "Score:", random_num, "Your grade is A"
scores_grades()