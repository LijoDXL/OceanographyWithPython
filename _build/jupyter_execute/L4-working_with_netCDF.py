# Gridded data, NetCDF

## Xarray
When working with higher dimensional data (3D or more), we can't rely on Pandas. Here comes [Xarray](http://xarray.pydata.org/en/stable/index.html) to the rescue.
* It has Pandas like syntax, so if you know Pandas you will find yourself at home with Xarray.
* format agnostic: It can read netCDF, GRIB, Zarr, raster files and also supports OPeNDAP.
* No need to convert between file formats (GRIB to netCDF and such) as Xarray gives similar interface for all supported data formats. 
* It works well with larger than memory datasets, and you can run parallel processes with minimum-to-no code change.
* It can save files in netCDF format as well, however does not impose CF convention by default.
* Though it is a general purpose tool, Xarray is developed keeping in mind the need of oceanographic community.

### Exercise
* read satellite measured Sea Surface Temperature (SST) [data](http://www.remss.com/measurements/sea-surface-temperature/) (accessible from data directory) in netCDF format.
* explore the data
* select a region and plot spatial SST
* select a few points and plot time series
* comapre SST for two days by plotting side by side in a subplot
* plot SST contour of greater than 30 degree Celcius
* add LAND and coastline to a plot
* change the projection of a plot

import xarray as xr
import numpy as np
import cmocean # for perceptually uniform colormaps
import cartopy as cr # for geographic mapping
import cartopy.crs as ccrs # for map projections
import matplotlib.pyplot as plt # plotting tool
import cartopy.feature as cfeature # to add coastlines, land and ocean
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

# reads a single netCDF file
ds = xr.open_dataset('data/remss/20190426120000-REMSS-L4_GHRSST-SSTfnd-MW_IR_OI-GLOB-v02.0-fv05.0.nc')

# data details along with metadata
ds

# variables in the dataset
ds.data_vars

# select one variable and plot
# since data is 2D meshgrid, it plots colormesh by default
ds.analysed_sst.plot()

# changing values in a variable
# here, SST is converted from degree Kelvin to degree Celcius
(ds.analysed_sst-273.15).plot(cmap='cmo.thermal')

# change is not affected unless it is saved to the variable
ds_sst = ds.analysed_sst - 273.15

# uncomment line to save data in netCDF
#ds_sst.to_netcdf('data/SSTinCelcius.nc')

# printsdata underneath a variable, which is numpy array
ds_sst.data

# shape of numpy array
ds_sst.data.shape

# coordinates can be accessed the same way as variables
ds_sst.time
# or ds_sst['time']

# selecting a region
ds_sst.sel(lon=slice(40,120),lat=slice(-30,30)).plot(cmap='cmo.thermal')

# read and combine many files along a dimension
ds_comb = xr.open_mfdataset('data/remss/*.nc',combine='by_coords')

# time coordinate now has 10 values instead of one
# data combined in time dimension
ds_comb

# shape of combined data
ds_comb.analysed_sst.shape

# time information was read in from each file and appended
ds_comb.time.data

# convert SST from degree Kelvin to degree Celcius
ds_sst_comb = ds_comb.analysed_sst - 273.15

# select a few points and plot time series
ds_sst_comb.sel(lat=[8,12,3],lon=90,method='nearest').plot(hue='lat',figsize=(12,4),marker='o')

# plot SST for two days (2019-04-29 and 2019-04-30) side by side
fig,ax = plt.subplots(1,2,figsize=(16,5),subplot_kw={'projection':ccrs.PlateCarree()})
ds_sst_comb.isel(time=3).sel(lon=slice(40,120),lat=slice(-30,30)).plot(ax=ax[0],cmap='cmo.thermal',levels=np.arange(20,35,1))
ds_sst_comb.isel(time=4).sel(lon=slice(40,120),lat=slice(-30,30)).plot(ax=ax[1],cmap='cmo.thermal',levels=np.arange(20,35,1))

# add land feature, coastlines and format lat lon labels
import go_land # see the file go_land.py
fig,ax = plt.subplots(1,2,figsize=(16,5),subplot_kw={'projection':ccrs.PlateCarree()})
ds_sst_comb.isel(time=4).sel(lon=slice(40,120),lat=slice(-30,30)).plot(ax=ax[0],cmap='cmo.thermal',levels=np.arange(20,35,1))
ds_sst_comb.isel(time=6).sel(lon=slice(40,120),lat=slice(-30,30)).plot(ax=ax[1],cmap='cmo.thermal',levels=np.arange(20,35,1))
for p in ax:
    go_land.fig_beauty(ax=p)

# add contours for temperatures above 30 degree Celcius
fig,ax = plt.subplots(figsize=(12,6),subplot_kw={'projection':ccrs.PlateCarree()})
cf = ds_sst_comb.isel(time=5).sel(lon=slice(40,120),lat=slice(-30,30)).plot.contourf(ax=ax,cmap='cmo.thermal',levels=np.arange(20,35,0.5))
c = ax.contour(cf,levels=np.arange(30,35,1),colors='black',linewidths=0.5)
ax.clabel(c,inline=True,fmt='%3.2f')

# change in plot projection
fig,ax = plt.subplots(subplot_kw={'projection':ccrs.Robinson()},figsize=(10,5))
ds_sst_comb.sel(time='2019-04-30').plot(ax=ax,transform=ccrs.PlateCarree())
ax.coastlines()
ax.add_feature(cfeature.LAND)

## Further resources
* Documentation [page](http://xarray.pydata.org/en/stable/index.html) for Xarray well explains use cases and has a lots of [examples](http://xarray.pydata.org/en/stable/examples.html) 
* [Workshop](https://nbviewer.jupyter.org/github/fmaussion/teaching/blob/master/xarray_intro_acinn/ACINN_workshop_xarray-slides.ipynb) by [Fabien Maussion](https://github.com/fmaussion) on Xarray usage 

