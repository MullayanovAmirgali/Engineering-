import random
import requests
from PIL import Image
from io import BytesIO

CITIES = ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань", "Нижний Новгород", "Челябинск", "Омск", "Самара"]

def get_city_image(city):
    image_url = f"https://via.placeholder.com/500.png?text={city}+Map"
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    return image

def guess_the_city():
    city = random.choice(CITIES)
    city_image = get_city_image(city)
    city_image.show()
    guess = input("Угадайте название города: ")
    if guess.lower() == city.lower():
        print("Правильно! Это", city)
    else:
        print("Неправильно. Правильный ответ:", city)

while True:
    input("Нажмите Enter, чтобы начать новый раунд...")
    guess_the_city()






