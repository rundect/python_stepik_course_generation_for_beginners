from random import choice

seq_upper = [chr(i) for i in range(65, 91)]
seq_lower = [chr(i) for i in range(97, 123)]
seq = seq_upper + seq_lower

length = int(input())    # длина пароля
for _ in range(length):
    print(choice(seq), end='')

