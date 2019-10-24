# don't be overwhelmed by this function
# the function just adds coastlines and formats
# the latitude longitude labeling
import cartopy as cr
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
def fig_beauty(ax,xlim=None,ylim=None,ocean=False):
    '''
       fig_beauty(ax,xlim,ylim,n)    ->   sets the aesthetics of the figure
       parameter : xlim: list
                         lower and upper lon values to set the plot extent
                   ylim: list
                         lower and upper lat values to set the plot extent
                     ax: matplotlib axes
                         axis of the plotted figure
                  ocean: Boolean
                         whether to add ocean 
    '''
    if xlim is not None:
        ax.set_xlim(xlim[0],xlim[1])
    if ylim is not None:
        ax.set_ylim(ylim[0],ylim[1]);
    ax.add_feature(cfeature.LAND)
    if ocean:
        ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.COASTLINE,)
    ax.set_ylabel('')
    ax.set_yticklabels('')
    gl=ax.gridlines(color='black',linestyle='--',alpha=0.15,linewidth=2)
    gl.xlabels_bottom=True
    gl.ylabels_left = True 
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER  
