import folium

# Create a map centered around the Monastery of St. Antony
map_center = [28.92402325344615, 32.34992348548081]
egypt_map = folium.Map(location=map_center, zoom_start=10)

# Add a pin for the Monastery of St. Antony
folium.Marker(
    location=map_center,
    popup="Monastery of St. Antony",
    icon=folium.Icon(color="red", icon="info-sign")
).add_to(egypt_map)

# Save the map to an HTML file
egypt_map.save("egypt_map.html")

print("Map with Monastery of St. Antony has been created.")
