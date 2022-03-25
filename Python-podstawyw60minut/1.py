point_x = 1
point_y = 2

# tupla, krotka - niemutowalne(niezmienne)
point = 1, 2
print(point[0])
print(point[1])
# point[0] = 2 nie zadziała w przypadku tupli
print(point)

# listy
cities = ['Gdynia', 'Gdańsk', 'Sopot']
print(cities[0])
print(cities[-1])
cities.append('Warszawa')
cities.append('Kraków')
cities.append('Katowice')
print(cities)
cities.sort()
cities[-1] = 'Zakopane'
print(cities)

# słowniki
capitals = {
    'Poland': 'Warszawa',
    'France': 'Paris',
    'Germany': 'Berlin'
}

print(capitals['Poland'])