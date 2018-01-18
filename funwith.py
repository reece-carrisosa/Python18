######## Odd/Even
def odd_even():
    x = 0
    for x in range(1,2001):
        if x % 2!=0:
            print "Number is", x, "This is an odd number."
        else:
            print "Number is", x, "This is an even number."
odd_even()

######### Multiply
def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b

######### Hacker Challenge
def layered_multiples(arr):
    a = []
    new_array = []
    for x in arr:
        print x
        for v in range(0,x):
            a.append(1)
        new_array.append(a)
        a = []
    return new_array
x = layered_multiples(multiply([2,4,5],3))
print x