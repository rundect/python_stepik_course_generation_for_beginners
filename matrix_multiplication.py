# put your python code here
n_a, m_a = [int(i) for i in input().split()]
matrix_a = [[int(i) for i in input().split()] for _ in range(n_a)]
input()
n_b, m_b = [int(i) for i in input().split()]
matrix_b = [[int(i) for i in input().split()] for _ in range(n_b)]
matrix_c = [[0] * m_b for _ in range(n_a)]


for i in range(n_a):
    for j in range(m_b):
        total = 0
        for k in range(m_a):
            total += (matrix_a[j][k] * matrix_b[k][i])
        matrix_c[j][i] = total
for row in matrix_c:
    print(*row, end='\n')