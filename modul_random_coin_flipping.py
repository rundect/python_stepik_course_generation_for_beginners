from random import randint

COIN = ['Орел', 'Решка']

for _ in range(int(input())):
    print(COIN[randint(0, 1)])

