import googlemaps
from datetime import datetime

def find_nearest_pharmacy(address):

    gmaps = googlemaps.Client(key='YOUR_API_KEY')

    try:
        geocode_result = gmaps.geocode(address)
        
        if geocode_result:
            location = geocode_result[0]['geometry']['location']
            latitude = location['lat']
            longitude = location['lng']

            pharmacies = gmaps.places_nearby(location=(latitude, longitude), radius=5000, type='pharmacy')
            
            if pharmacies['results']:
                nearest_pharmacy = pharmacies['results'][0]['name']
                return nearest_pharmacy
            else:
                return "Аптека не найдена."
        else:
            return "Не удалось найти координаты для указанного адреса."
    except Exception as e:
        return f"Ошибка: {str(e)}"

address = input("Введите адрес: ")

nearest_pharmacy = find_nearest_pharmacy(address)

print("Ближайшая аптека:", nearest_pharmacy)






