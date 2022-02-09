from random import randrange as r


def generate_ip():
    return f'{r(256)}.{r(256)}.{r(256)}.{r(256)}'


returned = generate_ip()
print(returned)
