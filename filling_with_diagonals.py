
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

counter = 1
row = 1
term = 0
for i in range(n):
    for j in range(m):
        if j <= n - i - 1:
            matrix[i][j] = counter
            term += 1
        else:
            counter += j
            matrix[i][j] = 0
        counter += term
    row += (i + 2)
    term -= 3
    counter = row

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()