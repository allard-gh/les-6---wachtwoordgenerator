import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!','@', '#', '$', '%', '^', '&', '(', ')', '*', '+', '_', '-', '=']

aantal_letters = int(input('Hoeveel letters wil je in je ww? '))
aantal_nummers = int(input('Hoeveel cijfers wil je in je ww? '))
aantal_symbolen = int(input('Hoeveel symbolen wil je in je ww? '))

ww = []

for i in range(aantal_letters):
    ww.append(random.choice(letters))

for i in range(aantal_nummers):
    ww.append(random.choice(numbers))

for i in range(aantal_symbolen):
    ww.append(random.choice(symbols))

random.shuffle(ww)

ww_shuffle = ''.join(ww)

print(ww_shuffle)