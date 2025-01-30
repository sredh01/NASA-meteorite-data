# NASA Meteorite Data Project

This project analyzes NASA meteorite data, performing clustering analysis and generating an interactive map. It includes **K-Means clustering** for mass vs. year distribution and an **interactive GeoJSON-based map**.

## Meteorite Clusters: Mass vs Year
The following scatter plot shows how meteorites are clustered based on mass and year using K-Means clustering:

*insert plot graph*

## Interactive Meteorite Map
This interactive map visualizes meteorite impact locations, allowing users to **click markers** for details:

*insert map*

Clicking on a marker reveals:
- **Name**
- **Latitude & Longitude**
- **Mass (g)**
- **Year of Impact**

## How to Run
1. **Install Dependencies**:
   ```bash
   pip install pandas numpy folium scikit-learn matplotlib tabulate
