for  - skończona ilość razy (ilość elementów, range())

for n in range(10):
    print(n)

for _ in range(10):
    print('Będę subskrybował ten kanał!')


while - wykonuje się dopóki twierdzenie jest prawdziwe

number_of_entries = 0
while number_of_entries < 30:
    entries = int(input('Ile osób wchodzi? '))
    number_of_entries += entries

    print('Razem osób: ', number_of_entries)


