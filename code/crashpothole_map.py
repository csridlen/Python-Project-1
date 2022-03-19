import os
import pandas as pd
from shapely.geometry import Point, Polygon
import geopandas as gpd
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt
import shapefile
import descartes

if __name__ == "__main__":
    os.makedirs("artifacts", exist_ok=True)

    # load and plot chicago zipcodes
    zips = "data/chicago_zipcodes.shp"
    map_zips = gpd.read_file(zips)
    fig, ax = plt.subplots(figsize=(15, 15))
    zip_plot = map_zips.plot(ax=ax, color="grey", alpha=0.5)

    # load traffic crashes csv and filter for missing points
    crash1 = pd.read_csv("data/crashes_1.csv")
    crash2 = pd.read_csv("data/crashes_2.csv")
    crashes = pd.concat([crash1, crash2])
    crashes = crashes.loc[crashes["LATITUDE"] != 0]
    crashes = crashes.loc[crashes["LONGITUDE"] != 0]

    # load pothold data and filter for missing points
    pot1 = pd.read_csv("data/potholes_1.csv")
    pot2 = pd.read_csv("data/potholes_2.csv")
    potholes = pd.concat([pot1, pot2])
    potholes = potholes.loc[potholes["LONGITUDE"] != 0]
    potholes = potholes.loc[potholes["LATITUDE"] != 0]
    potholes = potholes.loc[potholes["STATUS"] == "Open"]

    # create geodataframes
    crs = "epsg:4326"
    crash_geo = [Point(xy) for xy in zip(crashes["LONGITUDE"], crashes["LATITUDE"])]
    crash_gdf = GeoDataFrame(crashes, crs=crs, geometry=crash_geo)
    pothole_geo = [Point(xy) for xy in zip(potholes["LONGITUDE"], potholes["LATITUDE"])]
    pothole_gdf = GeoDataFrame(potholes, crs=crs, geometry=pothole_geo)

    # plot crashes and potholes on zipcode map
    map2 = crash_gdf.plot(
        ax=ax, markersize=10, color="red", marker="o", label="crashes"
    )
    map22 = pothole_gdf.plot(
        ax=ax, markersize=10, color="blue", marker="o", label="potholes"
    )

    # save figure as png
    mapf = map2.get_figure()
    mapf.savefig("artifacts/dualmap.png")
