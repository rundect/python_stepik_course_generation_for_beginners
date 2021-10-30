
def caesars_cipher(language, text, direction, step_of_shift):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    text_modified = ''
    correction = 0
    if direction == 0:
        step_of_shift = 0 - step_of_shift
        correction = 26
    for i in range(len(text)):
        if text[i].isalpha():
            if language == 'ru':
                if text[i] == text[i].lower():
                    alphabet = rus_lower_alphabet
                else:
                    alphabet = rus_upper_alphabet
            else:
                if text[i] == text[i].lower():
                    alphabet = eng_lower_alphabet
                else:
                    alphabet = eng_upper_alphabet
            text_modified += alphabet[alphabet.find(text[i]) - correction - step_of_shift]
        else:
            text_modified += text[i]
    return text_modified


language = input('Выберите язык текста (ru - русский, en - английский): ')
text = input('Введите текст: ')
direction = int(input('Вы хотите зашифровать текст или дешифровать его? (0 - зашифровать, 1 - дешифровать): '))
'''step_of_shift = int(input('Введите шаг сдвига: '))'''

for i in range(1, 26):
    print(i)
    step_of_shift = i
    text_modified = caesars_cipher(language, text, direction, step_of_shift)
    print(text_modified)

