import osmnx as ox
import geopandas as gpd
import os

OUT_DIR = r"c:\Users\Jinxxx\Desktop\Hussaini\SPE Africa Energython\data\gis"

# Lekki roughly:
north, south, east, west = 6.55, 6.40, 4.05, 3.80

print("Fetching OSM Data for Lekki...")

# 1. Industrial zones (for FTZ)
try:
    tags = {'landuse': 'industrial'}
    industrial = ox.features_from_bbox(bbox=(north, south, east, west), tags=tags)
    industrial.to_file(os.path.join(OUT_DIR, "lekki_ftz.geojson"), driver="GeoJSON")
    print("Saved industrial zones.")
except Exception as e:
    print(f"Failed industrial: {e}")

# 2. Roads (only primary/secondary to avoid huge files)
try:
    tags = {'highway': ['primary', 'secondary', 'tertiary', 'trunk']}
    roads = ox.features_from_bbox(bbox=(north, south, east, west), tags=tags)
    roads.to_file(os.path.join(OUT_DIR, "roads.geojson"), driver="GeoJSON")
    print("Saved roads.")
except Exception as e:
    print(f"Failed roads: {e}")

# 3. Water bodies
try:
    tags = {'natural': 'water', 'waterway': True}
    water = ox.features_from_bbox(bbox=(north, south, east, west), tags=tags)
    water.to_file(os.path.join(OUT_DIR, "water_bodies.geojson"), driver="GeoJSON")
    print("Saved water bodies.")
except Exception as e:
    print(f"Failed water bodies: {e}")

# 4. Substations / Power
try:
    tags = {'power': ['substation', 'plant', 'line']}
    power = ox.features_from_bbox(bbox=(north, south, east, west), tags=tags)
    power.to_file(os.path.join(OUT_DIR, "power.geojson"), driver="GeoJSON")
    print("Saved power infrastructure.")
except Exception as e:
    print(f"Failed power: {e}")

print("Done fetching vector data.")
