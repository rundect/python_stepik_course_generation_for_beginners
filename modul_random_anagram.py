from random import shuffle

s = input()
l = [i for i in s]
shuffle(l)
l = ''.join(l)
print(l)