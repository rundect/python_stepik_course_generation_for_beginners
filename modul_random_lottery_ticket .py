from random import randint

generated_set = set()

while len(generated_set) < 7:
    generated_set.add(randint(1, 49))

sorted_numbers = sorted(generated_set)
print(*sorted_numbers, sep=' ')
