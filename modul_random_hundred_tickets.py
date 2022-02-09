from random import randint

generated_set = set()

while len(generated_set) < 100:
    num = str(randint(1, 9))
    for i in range(6):
        num += str(randint(0, 9))
    generated_set.add(int(num))
for i in generated_set:
    print(i)
