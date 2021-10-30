def caesars_cipher(text):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text_modified = text.split()
    for i in range(len(text_modified)):
        counter = 0
        word_after_shift = ''
        for j in text_modified[i]:
            if j.isalpha():
                counter += 1
        for k in text_modified[i]:
            if k.islower():
                alphabet = eng_lower_alphabet
            else:
                alphabet = eng_upper_alphabet
            if k.isalpha():
                word_after_shift += alphabet[(alphabet.find(k) + counter) % 26]
            else:
                word_after_shift += k
        text_modified[i] = word_after_shift
    return text_modified


text = input()

text_modified = caesars_cipher(text)
print(*text_modified)
