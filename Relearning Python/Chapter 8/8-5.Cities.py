city_name = 'default name'
city_country = 'default country'
def describe_city(city_name, city_country):
    print(f'{city_name} is in {city_country}.')
    
describe_city(city_name, city_country)
describe_city('name_A', 'country_A')
describe_city(city_name, 'country_B')