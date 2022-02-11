from random import choice
from copy import copy

n = int(input())
list_of_names = [input() for i in range(n)]
list_for_comprehension = copy(list_of_names)
list_for_tuples = []

for i in list_of_names:
    j = choice(list_for_comprehension)
    if n < 3:
        while i == j:
            j = choice(list_for_comprehension)
        list_for_tuples.append([i, j])
        list_for_comprehension.remove(j)
    else:
        while i == j or ([j, i] in list_for_tuples):
            j = choice(list_for_comprehension)
        list_for_tuples.append([i, j])
        list_for_comprehension.remove(j)

for i in list_for_tuples:
    print(i[0], '-', i[1])
