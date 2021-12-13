from random import choice

txt = open('lines.txt')
print(choice(txt.readlines()))

txt.close()