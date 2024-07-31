import folium
import pandas as pd

# Define the coordinates of the locations
locations = [
    (-37.8043, 144.9631),  # Docklands
    (-37.8125, 144.9659),  # North Melbourne
    (-37.8157, 144.9709),  # Melbourne
    (-37.8174, 144.9746),  # Carlton
    (-37.8247, 144.9672),  # Flinders Street
    (-37.8045, 145.0081),  # Richmond
    (-37.7987, 145.0088),  # East Richmond
    (-37.8480, 145.0010),  # Hawksburn
]

# Create a list of distances between locations
distances = [
    [0, 2.4, 3.4, 3.0, 3.1, 4.6, 5.1, 7.1],
    [2.4, 0, 1.0, 1.4, 2.9, 4.2, 4.8, 6.9],
    [3.4, 1.0, 0, 1.8, 2.8, 3.9, 4.6, 6.6],
    [3.0, 1.4, 1.8, 0, 1.5, 3.2, 3.9, 5.9],
    [3.1, 2.9, 2.8, 1.5, 0, 2.3, 3.0, 5.0],
    [4.6, 4.2, 3.9, 3.2, 2.3, 0, 0.7, 2.8],
    [5.1, 4.8, 4.6, 3.9, 3.0, 0.7, 0, 2.1],
    [7.1, 6.9, 6.6, 5.9, 5.0, 2.8, 2.1, 0],
]

# Create a dataframe from the distances
df = pd.DataFrame(distances)

# Create a map centered on Melbourne
map = folium.Map(location=[-37.8136, 144.9631], zoom_start=12)

# Add markers for each location
for i, location in enumerate(locations):
    folium.Marker(location, popup=f"Location {i + 1}").add_to(map)

# Add lines between each pair of locations with the distance displayed
for i in range(len(locations)):
    for j in range(i + 1, len(locations)):
        folium.PolyLine(
            [locations[i], locations[j]],
            color="blue",
            weight=2.5,
            opacity=1,
            popup=f"{df.iloc[i, j]} km",
        ).add_to(map)

# Save the map as an html file
map.save("melbourne_map.html")

# Display the map in a jupyter notebook
from IPython.display import IFrame
IFrame(src="melbourne_map.html", width=900, height=600)