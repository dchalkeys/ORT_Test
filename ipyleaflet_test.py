#!/usr/bin/env python
# coding: utf-8

# # Generate Marker with Coordinates in Popup with User Click

# ### Imports

# In[1]:


import ipyleaflet
import geopandas as gpd
import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd
import base64
import folium
from shapely import Point
import altair
import ipywidgets
from ipywidgets import HTML



# In[2]:


m = ipyleaflet.Map(center=(0, 0), zoom=2)

def handle_click(**kwargs):
    if kwargs.get('type') == 'click':
        coords = kwargs.get('coordinates')
        lat = coords[0]
        lon = coords[1]
        popup_content = HTML(f"Latitude: {lat}<br>Longitude: {lon}")
        marker = ipyleaflet.Marker(location = coords, popup=ipyleaflet.Popup(child = popup_content), draggable = False)
        m.add_layer(marker)


m.on_interaction(handle_click)

m


# In[ ]:




