import folium

# Define the coordinates for each stadium
stadiums_location = {
    "Лужники": [55.715551, 37.554191],
    "Спартак": [55.818015, 37.440262],
    "Динамо": [55.791540, 37.559809]
}

moscow_map = folium.Map(location=[55.751244, 37.618423], zoom_start=11)

for stadium, coords in stadiums_location.items():
    folium.Marker(location=coords, popup=stadium).add_to(moscow_map)

moscow_map.save("/mnt/data/moscow_stadiums_map.html")

moscow_map
