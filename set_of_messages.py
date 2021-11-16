keyboard = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}

for letter in input().upper():
    for key, value in keyboard.items():
        if letter in value:
            print(key * (value.index(letter) + 1), end="")