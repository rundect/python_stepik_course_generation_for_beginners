
# put your python code here
s = [i for i in input()]

d_s = {}
for i in s:
    d_s[i] = d_s.get(i, 0) + 1

d = {}
for i in range(int(input())):
    key, value = input().split(': ')
    for j in d_s.items():
        if j[1] == int(value):
            d[j[0]] = key

for i in s:
    print(d[i], end='')
