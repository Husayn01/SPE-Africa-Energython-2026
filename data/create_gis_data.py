import os
import geopandas as gpd
from shapely.geometry import Point, LineString, Polygon, box

DATA_DIR = "gis"
os.makedirs(DATA_DIR, exist_ok=True)

# Using WGS84
crs_wgs84 = "EPSG:4326"

datasets = {
    "aoi.geojson": gpd.GeoDataFrame({"name": ["AOI"]}, geometry=[box(3.70, 6.30, 4.10, 6.70)], crs=crs_wgs84),
    "lekki_ftz.geojson": gpd.GeoDataFrame({"name": ["Lekki FTZ"]}, geometry=[box(3.82, 6.43, 3.98, 6.58)], crs=crs_wgs84),
    "elps_pipeline.geojson": gpd.GeoDataFrame({"name": ["ELPS spur"]}, geometry=[LineString([(3.80, 6.63), (3.82, 6.57), (3.84, 6.52), (3.86, 6.47), (3.89, 6.43)])], crs=crs_wgs84),
    "fiber_backbone.geojson": gpd.GeoDataFrame({"name": ["Fiber backbone"]}, geometry=[LineString([(3.90, 6.60), (3.91, 6.56), (3.93, 6.52), (3.96, 6.48), (4.00, 6.45)])], crs=crs_wgs84),
    "roads.geojson": gpd.GeoDataFrame({"name": ["Lekki Epe Expressway", "Internal access road"]}, geometry=[LineString([(3.73, 6.35), (3.82, 6.41), (3.93, 6.48), (4.05, 6.55)]), LineString([(3.84, 6.44), (3.88, 6.48), (3.95, 6.54)])], crs=crs_wgs84),
    "substations.geojson": gpd.GeoDataFrame({"name": ["132kV node", "330kV standby node"]}, geometry=[Point(3.90, 6.49), Point(4.01, 6.60)], crs=crs_wgs84),
    "water_bodies.geojson": gpd.GeoDataFrame({"name": ["Atlantic", "Lekki Lagoon"]}, geometry=[Polygon([(3.70, 6.30), (3.84, 6.30), (3.86, 6.38), (3.70, 6.38)]), Polygon([(3.77, 6.40), (3.96, 6.42), (4.03, 6.47), (3.97, 6.53), (3.83, 6.52), (3.75, 6.45)])], crs=crs_wgs84),
    "protected_zones.geojson": gpd.GeoDataFrame({"name": ["Conservation zone"]}, geometry=[Polygon([(3.76, 6.58), (3.82, 6.58), (3.83, 6.64), (3.75, 6.65)])], crs=crs_wgs84),
    "airports.geojson": gpd.GeoDataFrame({"name": ["Lekki airstrip"]}, geometry=[Point(3.95, 6.585)], crs=crs_wgs84),
    "workforce_centers.geojson": gpd.GeoDataFrame({"name": ["Lekki town", "Ajah", "Epe"]}, geometry=[Point(3.88, 6.46), Point(3.76, 6.50), Point(4.03, 6.57)], crs=crs_wgs84)
}

for filename, gdf in datasets.items():
    filepath = os.path.join(DATA_DIR, filename)
    gdf.to_file(filepath, driver="GeoJSON")
    print(f"Created {filepath}")

print("All GIS data files generated successfully.")
