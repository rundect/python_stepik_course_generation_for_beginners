from random import choice as c
from random import randrange as rr
from string import ascii_uppercase as letter


def generate_index():
    return f'{c(letter)}{c(letter)}{rr(100)}_{rr(100)}{c(letter)}{c(letter)}'


returned = generate_index()
print(returned)
