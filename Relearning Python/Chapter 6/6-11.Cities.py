"""
Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information you have stored about it
"""

cities = {
    'Atalnta': {
        'Country': 'Georgia',
        'Population': 300_000,
        'Fact': 'Random fact'
    },
    
    'Accra': {
        'Country': 'Ghana',
        'Population': 500_000,
        'Fact': 'Random fact'
    },
    
    'Phnom Penh': {
        'Country': 'Cambodia',
        'Population': 460_000,
        'Fact': 'Random fact'
    }
}

for city, info in cities.items(): 
    print(f'The city, {city}')
    for infos, value in info.items():
        print(f'\t{infos} : {value}')
