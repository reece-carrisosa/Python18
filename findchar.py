word_list = ['hello', 'world', 'my', 'name', 'is', 'Anna']
char = 'o'
new_list = []

for i in word_list:
    if i.find(char) != -1:
        new_list.append(i)
print new_list