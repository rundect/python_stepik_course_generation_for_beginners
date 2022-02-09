from random import randint

generated_set = set()
while len(generated_set) < 24:
    generated_set.add(randint(1, 75))

line = []
counter = 0
for i in generated_set:
    if counter == 12:
        line.append('0'.ljust(3))
        line.append(str(i).ljust(3))
        counter += 1
    elif counter % 4 == 0 and counter != 0:
        line.append(str(i).ljust(3))
        counter += 1
    else:
        line.append(str(i).ljust(3))
        counter += 1
    if len(line) == 5:
        print(*line)
        line = []
