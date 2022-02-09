
with open('nums.txt', encoding='utf-8') as file:
    total = 0
    for rows in file.readlines():
        rowtotal = '0'
        for char in rows:
            if char.isdigit():
                rowtotal += char
            else:
                total += int(rowtotal)
                rowtotal = '0'
    print(total)