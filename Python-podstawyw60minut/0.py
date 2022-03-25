print('Hello World')
first_name = input('Jak masz na imię? ')
print('Hello', first_name)

if first_name == 'Kacper':
    print('Cześć Kacper!')
else:
    print('Nie wiem kim jesteś, ale chętnie się dowiem!')

age = input('Ile masz lat? ')

if int(age) >= 18:
    print('Jesteś dorosły/a!')
else:
    print('Musisz jeszcze poczekać')
    wait_years = 18 - int(age)
    print('Będziesz dorosły za', wait_years, 'lat(a).')

# Operatory
# Matematyczne
# + - suma
# - - różnica
# * - iloczyn
# / - iloraz
# % - modulo (reszta z dzielenia) 5 % 2 == 1
# // - dzielenie całkowito liczbowe 5//2 == 2

# Logiczne
#  > większy
# < mniejszy
# >= większy lub równy
# <= mniejszy lub równy
# == równy
# != nierówny
#
# and, or, not
