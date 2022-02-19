
#### A function to plot SH and NH

def hemisphere_plot(
    northextent=None, southextent=None, figsize=None,
    fm_left=0.12, fm_right=0.88, fm_bottom=0.08, fm_top=0.96,
    ax_org = None,
    ):
    '''
    ----Input
    northextent: plot SH, north extent in degree south, e.g. -60, -30, or 0;
    southextent: plot NH, south extent in degree north, e.g. 60, 30, 0;
    figsize: figure size, e.g. np.array([8.8, 9.3]) / 2.54;
    fm_*: the space around four side of the graph
    ax_org: if specified, it will not create a new fig and ax.
    
    ----output
    (fig, ax): fig and ax object as returned by standard plotting function of matplotlib.
    
    ----function dependence
    None
    '''
    
    import numpy as np
    import matplotlib.pyplot as plt
    import cartopy.crs as ccrs
    import cartopy.feature as cfeature
    import matplotlib as mpl
    import matplotlib.path as mpath
    from cartopy.mpl.ticker import LongitudeFormatter
    from cartopy.mpl.ticker import LatitudeFormatter
    mpl.rc('font', family='Times New Roman', size=10)
    mpl.rcParams['figure.dpi'] = 600
    import warnings
    warnings.filterwarnings('ignore')
    
    if (figsize is None):
        figsize = np.array([8.8, 9.3]) / 2.54
    
    if not (northextent is None):
        # If you specified northextent, this function will plot SH. And it will ignore 'southextent'.
        projections = ccrs.SouthPolarStereo()
        extent = (-180, 180, -90, northextent)
        yticks = np.arange(-90, northextent + 1, 10)
    elif not (southextent is None):
        projections = ccrs.NorthPolarStereo()
        extent = (-180, 180, southextent, 90)
        yticks = np.arange(southextent - 1, 90, 10)
    
    transform = ccrs.PlateCarree()
    
    if (ax_org is None):
        fig, ax = plt.subplots(
            1, 1, figsize=figsize, subplot_kw={'projection': projections},
            )
    else:
        ax = ax_org
    
    ax.set_extent(extent, crs=transform)
    
    coastline = cfeature.NaturalEarthFeature(
        'physical', 'coastline', '10m', edgecolor='black',
        facecolor='none', lw=0.25)
    ax.add_feature(coastline, zorder=2)
    borders = cfeature.NaturalEarthFeature(
        'cultural', 'admin_0_boundary_lines_land', '10m',
        edgecolor='black', facecolor='none', lw=0.25)
    ax.add_feature(borders, zorder=2)
    
    gl = ax.gridlines(
        crs=transform, linewidth=0.15, zorder=2,
        draw_labels=True, color='gray', alpha=0.5, linestyle='--',
        xlocs=np.arange(-180, 181, 30), ylocs=yticks, rotate_labels=False,
        xformatter=LongitudeFormatter(degree_symbol='° '),
        yformatter=LatitudeFormatter(degree_symbol='° '),
    )
    gl.ylabel_style = {'size': 0, 'color': None, 'alpha': 0}
    
    # set circular axes boundaries
    theta = np.linspace(0, 2*np.pi, 100)
    center, radius = [0.5, 0.5], 0.5
    verts = np.vstack([np.sin(theta), np.cos(theta)]).T
    circle = mpath.Path(verts * radius + center)
    ax.set_boundary(circle, transform=ax.transAxes)
    
    plt.setp(ax.spines.values(), linewidth=0.2)
    
    if (ax_org is None):
        fig.subplots_adjust(
            left=fm_left, right=fm_right, bottom=fm_bottom, top=fm_top)
        return fig, ax
    else:
        return ax


#### A function to plot the global map

def globe_plot(
    figsize=None,
    fm_left=0.12, fm_right=0.94, fm_bottom=0.1, fm_top=0.99,
    ax_org = None,
    ):
    '''
    ----Input
    figsize: if by default None, it is set as: np.array([13.2, 6.6]) / 2.54
    fm_*: the space around four side of the graph
    ax: if specified, it will not create a new fig and ax.
    
    ----output
    
    '''
    import numpy as np
    import cartopy as ctp
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    from cartopy.mpl.ticker import LongitudeFormatter
    from cartopy.mpl.ticker import LatitudeFormatter
    
    mpl.rcParams['figure.dpi'] = 600
    mpl.rc('font', family='Times New Roman', size=10)
    
    if (figsize is None):
        figsize = np.array([13.2, 6.6]) / 2.54
    
    if (ax_org is None):
        fig, ax = plt.subplots(
            nrows=1, ncols=1,
            figsize = figsize, # figure size in inches
            subplot_kw={'projection': ctp.crs.PlateCarree()},
            )
    else:
        ax = ax_org
    
    ax.set_extent(
        [-180, 180, -90, 90],
        crs = ctp.crs.PlateCarree(),
        )
    
    coastline = ctp.feature.NaturalEarthFeature(
        'physical', 'coastline', '10m', edgecolor='black',
        facecolor='none', lw = 0.1)
    ax.add_feature(coastline)
    borders = ctp.feature.NaturalEarthFeature(
        'cultural', 'admin_0_boundary_lines_land', '10m', edgecolor='black',
        facecolor='none', lw = 0.1)
    ax.add_feature(borders)
    
    gl = ax.gridlines(
        crs = ctp.crs.PlateCarree(), linewidth = 0.1,
        color = 'gray', alpha = 0.5, linestyle='--',
        xlocs=np.arange(-180, 181, 60), ylocs=np.arange(-90, 91, 30),
        draw_labels=["bottom", "left"],
        xformatter=LongitudeFormatter(degree_symbol='° '),
        yformatter=LatitudeFormatter(degree_symbol='° '),
        )
    
    if (ax_org is None):
        fig.subplots_adjust(
            left=fm_left, right = fm_right, bottom = fm_bottom, top = fm_top)
        return fig, ax
    else:
        return ax
