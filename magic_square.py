n = 8
matrix = []
counter = 0
for i in range(97, 105):
    matrix.append([])
    for j in range(n, 0, -1):
        s = chr(i) + str(j)
        matrix[counter].append(s)
    counter += 1

x = input()
for i in range(n):
    for j in range(n):
        if matrix[i][j] == x:
            c = i
            r = j
list_of_steps = []
for i in range(-2, 3):
    for j in range(-2, 3):
        if i == 0 or j == 0 or (abs(i) == abs(j)):
            continue
        else:
            row = r + i
            col = c + j
            if 0 <= row and 0 <= col:
                list_of_steps.append(str(row) + str(col))
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if str(i) + str(j) in list_of_steps:
            matrix[i][j] = '*'
        else:
            matrix[i][j] = '.'
matrix[r][c] = 'N'
for ro in matrix:
    print(*ro)
