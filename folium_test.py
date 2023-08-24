#!/usr/bin/env python
# coding: utf-8

# # Generate Time Series Plot Popup from Test Coordinates

# ## Imports

# In[17]:


import geopandas as gpd
import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd
import base64
from folium import IFrame
import folium


# ### Declare Test Coordinates to Point and Retrieve Time Series

# In[ ]:


# Good snowfall spot
event = Point((48.7767, 121.8144))

clicked_point = Point(event.x, event.y)

point_dist = gdf.distance(clicked_point)
closest_points = gdf[point_dist==point_dist.min()]

closest_points


# ### Declare Chart Properties and Create Time Series Plot

# In[18]:


width = 300
height = 200


vega_data = altair.Chart(closest_points, width=width, height=height).mark_line().encode(
    x = 'time:T',
    y = 'sd:N'
)
vega_data


# ### Declare Marker Propertiers and Plot Marker on Map with Popup Time Series Plot

# In[19]:


lat = event.x
lon = event.y

m = folium.Map(location=[lat, lon], zoom_start=15)

marker = folium.Marker(
    location=[lat, lon],
    popup=folium.Popup(max_width=450).add_child(
        folium.VegaLite(vega_data, width=450, height=250)
    ),
)

marker.add_to(m)

m

