import pandas as pd
from shapely.geometry import Point, Polygon
import geopandas as gpd
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt
import shapefile
import descartes


# load and plot chicago zipcodes 
zips = 'data/chicago_zipcodes.shp'
# zips_geo = shapefile.Reader(zips).__geo_interface__
# zips1 = gpd.read_file(zips)
# zips1 = zips1.to_crs(epsg = 4326)
map_zips = gpd.read_file(zips)
fig,ax = plt.subplots(figsize = (15,15))
zip_plot = map_zips.plot(ax = ax, color='grey', alpha = 0.4)



# load pothold data and filter for missing points
pot1 = pd.read_csv('data/potholes_1.csv')
pot2 = pd.read_csv('data/potholes_2.csv')
potholes = pd.concat([pot1, pot2])
potholes = potholes.loc[potholes['LONGITUDE'] != 0]
potholes = potholes.loc[potholes['LATITUDE'] != 0]
completed = potholes.loc[potholes['STATUS'] == 'Completed']
opened = potholes.loc[potholes['STATUS'] == 'Open']


# create geodataframe
crs = {'init': 'epsg:4326'}
completed_geo = [Point(xy) for xy in zip(completed['LONGITUDE'], completed['LATITUDE'])]
completed_gdf = GeoDataFrame(completed, crs = crs, geometry=completed_geo)
opened_geo = [Point(xy) for xy in zip(opened['LONGITUDE'], opened['LATITUDE'])]
opened_gdf = GeoDataFrame(opened, crs = crs, geometry=opened_geo)

# plot crashes and potholes on zipcode map
map2 = completed_gdf.plot(ax = ax, markersize = 10, color = 'grey', marker = 'o', label = 'Completed')
map2 = opened_gdf.plot(ax = ax, markersize = 10, color = 'blue', marker = 'o', label = 'Open')

# save figure as png
map2.set_title(label = 'Potholes by Status', fontsize = 24, loc = 'center')
map2.legend(loc = 'upper left')
mapf = map2.get_figure()
mapf.savefig("artifacts/pothole_status_map.png")

  