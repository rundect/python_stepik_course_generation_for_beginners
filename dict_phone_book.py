# put your python code here
d = {}
for i in range(int(input())):
    value, key = input().split()
    d.setdefault(key.lower(), []).append(value)

list_of_countries = []
for i in range(int(input())):
    a = d.get(input().lower(), ['абонент не найден'])
    list_of_countries.append(a)

for i in list_of_countries:
    print(*i)