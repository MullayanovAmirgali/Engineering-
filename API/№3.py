from PIL import Image, ImageDraw

x = float(input("Введите координату x объекта: ")) 
y = float(input("Введите координату y объекта: ")) 

width, height = 64, 64 
image = Image.new("RGB", (width, height), "blue")  
draw = ImageDraw.Draw(image) 

draw.point((int(x), int(y)), fill="white")

image.save("Спутниковый снимок.png")

print("Снимок сохранен в файл СнимокЗадание3.png")





