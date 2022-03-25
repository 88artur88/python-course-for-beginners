from random import choice

capitals = {
    'Poland': 'Warszawa',
    'France': 'Paris',
    'Germany': 'Berlin'
}

# Google: 'How to select random key of dictionary in Python?'

selected_country = choice(list(capitals.keys()))

capital = input(f'What is the capital of {selected_country}? ')
if capitals[selected_country] == capital:
    print('Bardzo dobrze!')
else:
    print('Wcale nie! chodziło nam o', capitals[selected_country])
