from random import choice
from copy import copy

n = int(input())
list_of_names = [input() for i in range(n)]
list_for_comprehension = copy(list_of_names)
print(id(list_of_names))
print(id(list_for_comprehension))

for i in list_of_names:
    print(list_of_names)
    j = choice(list_for_comprehension)
    while i == j:
        j = choice(list_for_comprehension)
    list_for_comprehension.remove(j)
    print(i, '-', j)
