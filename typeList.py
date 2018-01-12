l = ['magical unicorns', 19, 'hello', 401, 'world']

newString = " "
sum = 0
decisionString = 0
decisionInt = 0
decisionFloat = 0

for i in l:
    if isinstance(i, str):
        newString += i
        decisionString += 1
    elif isinstance(i, int):
        sum += i
        decisionInt += 1
    elif isinstance(i, float):
        sum += i
        decisionFloat += 1

if (decisionString > 0 and decisionInt > 0 and decisionFloat > 0):
    print "The array you entered is of mixed type"
elif (decisionString > 0 and decisionInt ==0 and decisionFloat == 0):
    print "The array you entered is of string type"
elif (decisionString == 0 and decisionInt > 0 and decisionFloat > 0):
    print "The array you entered is of integer type"
print sum, newString