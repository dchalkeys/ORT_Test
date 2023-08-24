#!/usr/bin/env python
# coding: utf-8

# # Imports

# In[1]:


import base64

import bqplot.pyplot as plt
import geopandas as gpd
import ipyleaflet
import ipywidgets
import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd
import xarray as xr
from shapely import Point

# # Open File in GeoPandas

# In[2]:


# Open w/ xarray
nc_file = "download_Xsmall.nc"
ds = xr.open_dataset(nc_file)
ds


#
# # Extract Snow Water Equivalent

# In[3]:


sdwe = ds["sd"]
sdwe


# # Convert to Pandas Dataframe

# In[5]:


df = sdwe.to_dataframe().reset_index()
df


# # Convert to Geopandas Dataframe

# In[6]:


gdf = gpd.GeoDataFrame(
    df[["sd", "time"]], geometry=gpd.points_from_xy(df.longitude, df.latitude)
)

gdf


# # Filter out null values

# In[7]:


gdf = gdf[~gdf["sd"].isna()]
gdf


# # Filter out 10's (too many to not be suspicous)

# In[8]:


gdf = gdf[gdf["sd"] != 10]
gdf


# # Print Summary Statistics

# In[ ]:


gdf_reset_index = gdf.reset_index()

numeric_columns = gdf_reset_index.select_dtypes(include=["float32", "int64"])
summary_stats = numeric_columns["sd"].describe()
print(summary_stats)
print(gdf_reset_index.columns)


# # Define Functions

# In[9]:


m = ipyleaflet.Map(center=(0, 0), zoom=2)


def create_plot(x, y):
    fig = plt.figure()
    plt.plot(x, y)
    fig.layout.width = "325px"
    fig.layout.height = "250px"
    return fig


def get_closest_points(lat, lon):
    clicked_point = Point(lat, lon)
    point_dist = gdf.distance(clicked_point)
    closest_points = gdf[point_dist == point_dist.min()]
    return closest_points


def handle_clicks(**kwargs):
    if kwargs.get("type") == "click":
        # get coordinates of mouseclick
        coords = kwargs.get("coordinates")
        lat = coords[0]
        lon = coords[1]

        closest_points = get_closest_points(lat, lon)

        fig = create_plot(closest_points["time"], closest_points["sd"])

        # create marker and insert plot into popup
        marker = ipyleaflet.Marker(
            location=coords,
            popup=ipyleaflet.Popup(child=fig, width=500, height=300),
            draggable=False,
        )

        m.add_layer(marker)


# # Call Map

# In[11]:


m.on_interaction(handle_clicks)

m
