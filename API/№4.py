def find_southernmost_city(cities):

    southernmost_city = None

    min_latitude = float('inf')


    cities_list = cities.split(',')


    for city in cities_list:

        city = city.strip()

        if not city.isalpha():
            print(f"Город '{city}' имеет неправильный формат. Город должен состоять только из букв.")
            continue

        latitude_input = input(f"Введите широту города {city}: ")

        if not latitude_input.replace('.', '').replace('-', '').isdigit():
            print("Широта должна быть числом.")
            continue

        latitude = float(latitude_input)

        if latitude < min_latitude:
            min_latitude = latitude
            southernmost_city = city

    return southernmost_city


city_input = input("Введите список городов через запятую: ")


southernmost_city = find_southernmost_city(city_input)


if southernmost_city:
    print(f"Самый южный город: {southernmost_city}")
else:
    print("Не удалось определить самый южный город.")






