import folium  
from folium import plugins 
import numpy as np 

def calculate_distance(coords):
    total_distance = 0
    for i in range(len(coords) - 1):
        lat1, lon1 = coords[i]
        lat2, lon2 = coords[i+1]
        radius = 6371  
        dlat = np.radians(lat2 - lat1)
        dlon = np.radians(lon2 - lon1)
        a = np.sin(dlat / 2) * np.sin(dlat / 2) + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon / 2) * np.sin(dlon / 2)
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
        distance = radius * c
        total_distance += distance
    return total_distance

def main():
    points_sequence = [(54.734768,55.957838), (55.755773,37.617761),(57.153033,65.534328)]
    total_distance = calculate_distance(points_sequence)
    print("Total distance of the path:", total_distance, "km")
    midpoint_index = len(points_sequence) // 2
    midpoint = points_sequence[midpoint_index]
    map_center = midpoint
    my_map = folium.Map(location=map_center, zoom_start=5)
    for point in points_sequence:
        folium.Marker(point).add_to(my_map)
    folium.Marker(midpoint, icon=folium.Icon(color='red')).add_to(my_map)
    folium.PolyLine(locations=points_sequence, color='blue').add_to(my_map)
    my_map.save("dlina_puti.html")
if __name__ == "__main__":
    main()