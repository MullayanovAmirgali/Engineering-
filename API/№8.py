import math 

def calculate_distance(lat1, lon1, lat2, lon2):
    
    lat1 = math.radians(lat1) 
    lon1 = math.radians(lon1)  
    lat2 = math.radians(lat2) 
    lon2 = math.radians(lon2) 

    delta_lat = lat2 - lat1  
    delta_lon = lon2 - lon1

    cos_avg_lat = math.cos((lat1 + lat2) / 2)  

    distance = math.sqrt((111 * delta_lat) ** 2 + (111 * cos_avg_lat * delta_lon) ** 2)

    return distance 

def main():
    home_lat = float(input("Введите широту дома: ")) 
    home_lon = float(input("Введите долготу дома: ")) 

    uni_lat = float(input("Введите широту университета: ")) 
    uni_lon = float(input("Введите долготу университета: ")) 

    distance = calculate_distance(home_lat, home_lon, uni_lat, uni_lon)

    print("Расстояние от дома до университета составляет {:.2f} км.".format(distance))

if __name__ == "__main__":
    main()  






