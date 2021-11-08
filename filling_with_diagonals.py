
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

row = 1
minus = 1
for i in range(n):
    counter = row
    for j in range(m):
        if j <= n - i - 1:
            counter += (j + i)
            matrix[i][j] = counter
        else:
            counter += (j - )
            matrix[i][j] = counter
    row += (i + 1)


for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
