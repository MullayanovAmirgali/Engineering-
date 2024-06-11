import sys 
import requests

def get_district(address): 
    try: 
        url = 'https://geocode-maps.yandex.ru/1.x'
        params = {
            'apikey': 'api_key',
            'format': 'json',
            'geocode': address
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()


        pos = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
        longitude, latitude = float(pos[0]), float(pos[1])


        url = 'https://geocode-maps.yandex.ru/1.x'
        params = {
            'apikey': 'api_key',
            'format': 'json',
            'geocode': f'{longitude},{latitude}',
            'kind': 'district'
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        district = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['name']

        return district 

    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Укажите адрес")
        sys.exit(1)

    address = ' '.join(sys.argv[1:])
    district = get_district(address)


    if district:
        print(f"Адрес '{address}' находится в районе {district}.")
    else:
        print("Не удалось определить район для данного адреса.")





