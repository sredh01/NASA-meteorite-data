import numpy as np
import pandas as pd
import folium
from tabulate import tabulate
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the Nasa Dataset
file = 'NASA_MeteoriteData_Raw.csv'
pd.options.display.width = 0
data = pd.read_csv(file)
data.dropna(inplace=True)

# Refactor the NASA data to make it more readable in CSV format. Put in ID number order.
NASAFile = "NASA_MeteoriteData_Refactored.csv"
data.to_csv(NASAFile, index=False)
NASATable = tabulate(data, headers='keys', tablefmt='fancy_grid', showindex=False)
with open('NASA_MeteoriteData_Refactored.csv', 'w') as file:
    file.write(NASATable)

# Clustering portion
values = ['mass', 'year']
selectedFeatures = data[values]
cluster_num = 8

Kmeans = KMeans(n_clusters=cluster_num, random_state=42, n_init=10)
data['cluster'] = Kmeans.fit_predict(selectedFeatures)

markers = ['o', '^', '>', '<', 'v', '*', 'p', 'X']
colormap = plt.colormaps.get_cmap("tab10")
colors = [colormap(i / cluster_num) for i in range(cluster_num)]

for cluster in range(cluster_num):
    cluster_data = data[data['cluster'] == cluster]

    # Add jitter (scaled to mass for better visualization)
    jitter_strength = cluster_data['mass'].std() * 0.1
    jitter = np.random.normal(0, jitter_strength, size=len(cluster_data))

    plt.scatter(
        cluster_data['mass'] + jitter, cluster_data['year'],
        alpha=0.7, marker=markers[cluster % len(markers)],
        label=f'Cluster {cluster + 1}', color=colors[cluster]
    )

plt.xscale('log')
plt.title('Meteorite Clusters: Mass vs Year', fontsize=14, fontweight='bold')
plt.xlabel('Mass (g) (Log Scale)', fontsize=12)
plt.ylabel('Year', fontsize=12)
plt.ylim(1350, 2200)
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


def create_meteorite_map_geojson(data):
    """Generates an interactive meteorite impact map using GeoJSON for better performance."""

    # Remove rows with missing lat/long (prevents errors)
    data = data.dropna(subset=['lat', 'long'])

    # Create a map centered at the average lat/long
    the_map = folium.Map(location=[data['lat'].mean(), data['long'].mean()], zoom_start=2)

    # Convert DataFrame to GeoJSON format
    geojson_features = []
    for _, row in data.iterrows():
        feature = {
            "type": "Feature",
            "properties": {
                "popup": (
                    f"<b>Name:</b> {row['name']}<br>"
                    f"<b>Latitude:</b> {row['lat']}<br>"
                    f"<b>Longitude:</b> {row['long']}<br>"
                    f"<b>Mass:</b> {row['mass']} g<br>"
                    f"<b>Year:</b> {row['year']}"
                )
            },
            "geometry": {
                "type": "Point",
                "coordinates": [row["long"], row["lat"]]
            }
        }
        geojson_features.append(feature)

    geojson_data = {
        "type": "FeatureCollection",
        "features": geojson_features
    }

    folium.GeoJson(
        geojson_data,
        name="Meteorites",
        popup=folium.GeoJsonPopup(fields=["popup"], labels=False)
    ).add_to(the_map)
    # Save the map
    the_map.save("meteor_map.html")
    print("New optimized meteorite map using GeoJSON created: meteor_map.html")

# Generate the map
create_meteorite_map_geojson(data)
