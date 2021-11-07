
def chessboard(s):
    n = int(s[0])
    m = int(s[1])
    print(s, n, m)
    for i in range(n):
        if i % 2 == 0:
            counter = -1
        else:
            counter = 0
        for j in range(m):

            if j % 2 == 0:
                counter += 1
            else:
                counter -= 1
            return s


s = input().split()
result = chessboard(s)
print(result)
