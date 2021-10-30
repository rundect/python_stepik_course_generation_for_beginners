n, k = [i + 1 for i in range(int(input()))], int(input())
i = 0
while len(n) != 1:
    if (i + k) % len(n) == 0:
        m = len(n) - 1
    else:
        m = (((i + k) % len(n)) - 1)
    n.remove(n[m])
    i = m
print(*n)