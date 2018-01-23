######## Stars
b = ['Reece', 2, 'Sam', 7, 9]
def draw_stars(arr):
    for x in arr:
        if type(x) == int:
             print "*"*x
        else:
             print x[0].lower()*len(x)
        

draw_stars(b)