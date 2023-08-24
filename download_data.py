#!/usr/bin/env python
# coding: utf-8


import cdsapi

c = cdsapi.Client()

# download xsmall data - just one hour of one day for three days
c.retrieve(
    "reanalysis-era5-land",
    {
        "variable": "snow_depth_water_equivalent",
        "year": "2022",
        "time": ["12:00"],
        "day": [
            "29",
            "30",
            "31",
        ],
        "month": "12",
        "format": "netcdf",
    },
    "download_Xsmall.nc",
)
