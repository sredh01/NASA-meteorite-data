# NASA Meteorite Data Project

This project analyzes NASA meteorite data, performing clustering analysis and generating an interactive map. It includes **K-Means clustering** for mass vs. year distribution and an **interactive GeoJSON-based map**.

## Meteorite Clusters: Mass vs Year
The following scatter plot shows how meteorites are clustered based on mass and year using K-Means clustering:

<img width="639" alt="MeteoriteClusters" src="https://github.com/user-attachments/assets/c33fb306-e0d0-463e-83ba-4e200d1f1a96" />

## Interactive Meteorite Map
This interactive map visualizes meteorite impact locations, allowing users to **click markers** for details:

<img width="1512" alt="MeteoriteMap" src="https://github.com/user-attachments/assets/ebacd276-52df-4e27-93e0-cf9ae47aef4d" />

Clicking on a marker reveals:
- **Name**
- **Latitude & Longitude**
- **Mass (g)**
- **Year of Impact**

## How to Run
1. **Install Dependencies**:
   ```bash
   pip install pandas numpy folium scikit-learn matplotlib tabulate
