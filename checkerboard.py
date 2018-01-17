# x = "* * * *"
# y = " * * * *"
# l = 1
# while l <= 4:
#     print x
#     print y
#     l +=1

# for x in range(1,6):
#     print (5-x)*' ' + " ".join(['*']*x)



# def pattern(n):
#     for x in range( 1, n+1 ):
#         print (n-x)*' ' + " ".join(['*']*x)
# pattern(30)


def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b