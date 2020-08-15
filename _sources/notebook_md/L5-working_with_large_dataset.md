---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.5.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Dask
* A [package](https://dask.org/) which facilitates chunking of data to fit in memory and parallelism to your code
* Setup is as simple as enable it and forget
* It integrates with popular packages like Numpy, Pandas and Xarray, so no additional syntaxes to learn.
* Can be [deployed](https://docs.dask.org/en/latest/setup.html) on simple laptops, HPCs and even on cloud computers.


# Exercise
* Open OSCAR surface ocean currents (large dataset with 10 GB size) and chunk it
* compute monthly mean currents using all cores of your cpu
* use 3D ocean data (EN4) to draw temperature and salinity vertical profile

The data is too large to be distributed through Github. You can dowload the data from link below:
* OSCAR: https://podaac.jpl.nasa.gov/dataset/OSCAR_L4_OC_third-deg
* EN4: https://www.metoffice.gov.uk/hadobs/en4/

```python
import xarray as xr
import numpy as np
import cmocean
import cartopy as cr
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
```

```python
%matplotlib inline
```

```python
from dask.distributed import Client
from dask.diagnostics import ProgressBar
client = Client() # your local cluster
client # click the dashboard link to visualize the task and worker status
```

```python
ds = xr.open_dataset('/home/lijo/WORK/oceanCurrValidation/data/oscar_data/oscar_vel2003_2011.nc',chunks={'latitude':100,'latitude':1000,'time':10})
```

```python
ds.nbytes/1e9
```

```python
ds
```

```python
ds.time
```

```python
ds_mean = ds.groupby('time.month').mean().compute()
```

```python
ds_mean.sel(latitude=slice(30,-30),longitude=slice(60,120),month=[4,6,9,10]).u.plot(col='month',col_wrap=2,levels=np.arange(-1,1,0.1))
```

```python
ds_en4 = xr.open_dataset('/home/lijo/WORK/oceanCurrValidation/data/en42003-2010.nc',decode_times=False)
```

```python
ds_en4
```

```python
ds_en4.nbytes/1e9
```

```python
ds_temp = ds_en4.sel(LAT=slice(10,12),LON=slice(80,82)).isel(TMON=5).TEMP
ds_sal = ds_en4.sel(LAT=slice(10,12),LON=slice(80,82)).isel(TMON=5).SAL
t = xr.where(ds_temp<1000,ds_temp,np.nan) - 273.15
s = xr.where((ds_sal<1000) & (ds_sal>10),ds_sal,np.nan)
```

```python
fig,ax = plt.subplots(figsize=(5, 6))
t.mean(dim=['LAT','LON']).plot(ax=ax,y='DEPTH',yincrease=False,ylim=(500,0),color='r')
ax2 = ax.twiny()
s.mean(dim=['LAT','LON']).plot(ax=ax2,y='DEPTH',yincrease=False,ylim=(500,0),color='b')
for ticklabel in ax.get_xticklabels():
    ticklabel.set_color('r')
for ticklabel in ax2.get_xticklabels():
    ticklabel.set_color('b')
```

# Further resources
* Documentation [page](https://docs.dask.org/en/latest/)
* Dask+Xarray [tutorial](https://github.com/pangeo-data/pangeo-tutorial-sea-2018/tree/master/notebooks)
* Dask [tutorial](https://github.com/dask/dask-tutorial)
* [Example](https://pangeo.io/use_cases/physical-oceanography/sea-surface-height.html) of cloud computing using dask
* Follow Matthew Rocklin's [blog](http://matthewrocklin.com/blog/)

```python

```
