i = input()
s = i + ' запретил букву '
counter = 1072
while s != '' and (s.isspace() is not True):
    if s.find(chr(counter)) != -1:
        s = s.replace('  ', ' ')
        print((s + chr(counter)).strip())
        while s.find(chr(counter)) != -1:
            s = s[:s.find(chr(counter))] + s[s.find(chr(counter)) + 1:]
        counter += 1
    else:
        counter += 1