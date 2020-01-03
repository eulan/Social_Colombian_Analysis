# -*- coding: utf-8 -*-
"""folium.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_DRewn6qO3HQhyFq0L5qm6npgtDpWq6Q
"""

from google.colab import drive
drive.mount('/content/gdrive')

!pip install -q matplotlib-venn
!sudo apt-get install libgeos-3.5.0
!sudo apt-get install libgeos-dev
!sudo pip install https://github.com/matplotlib/basemap/archive/master.zip

path = '/content/gdrive/My Drive/Colab Notebooks/folium/INMISIONES_-_DATOS_DE_CONTAMINANTES_Y_CLIMATOL_GICOS_2016.csv'

import pandas as pd 
df = pd.read_csv(path)
df.head()

latitude = 4.570868
longitude = -74.2973328
df['Max_index_quartile'] = pd.qcut(df['Máximo'], 4, labels=False)
df.head()

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
from mpl_toolkits.axes_grid1.colorbar import colorbar
import numpy as np
from numpy import meshgrid

gp = df.groupby(['Variable'])

gp.first()

fig = plt.figure(figsize=(15, 20))

# Mapa 1
ax = fig.add_subplot(3,3,1)
ax.set_title('CO')
m = Basemap(
    ax = ax,
    resolution = 'i',
    projection = 'merc',
    llcrnrlon = -79, llcrnrlat = -5,
    urcrnrlon = -65.537390, urcrnrlat = 11.934540 
)
m.drawcoastlines(color='gray')
m.drawcountries(color='black')
m.drawstates(color='gray')
m.etopo(scale=0.2, alpha=0.3)
lat = gp.get_group('CO') ['Latitud'].values
lon = gp.get_group('CO') ['Longitud'].values
maximos = gp.get_group('CO') ['Máximo'].values
area = gp.get_group('CO') ['Máximo'].values
plotter = m.scatter(lon, lat, latlon=True,
          c=maximos, s=area,
          cmap='viridis', alpha=2)
cb = fig.colorbar(plotter, ax=ax)

 # Mapa 2
ax = fig.add_subplot(3,3,2)
ax.set_title('NO')
m = Basemap(
    ax = ax,
    resolution = 'i',
    projection = 'merc',
    llcrnrlon = -79, llcrnrlat = -5,
    urcrnrlon = -65.537390, urcrnrlat = 11.934540 
)
m.drawcoastlines(color='gray')
m.drawcountries(color='black')
m.drawstates(color='gray')
m.etopo(scale=0.2, alpha=0.3)
lat = gp.get_group('NO') ['Latitud'].values
lon = gp.get_group('NO') ['Longitud'].values
maximos = gp.get_group('NO') ['Máximo'].values
area = 10*gp.get_group('NO') ['Máximo'].values
plotter = m.scatter(lon, lat, latlon=True,
          c=maximos, s=area,
          cmap='viridis', alpha=2)
cb = fig.colorbar(plotter, ax=ax)
 # Mapa 3
ax = fig.add_subplot(3,3,3)
ax.set_title('NO2')
m = Basemap(
    ax = ax,
    resolution = 'i',
    projection = 'merc',
    llcrnrlon = -79, llcrnrlat = -5,
    urcrnrlon = -65.537390, urcrnrlat = 11.934540 
)
m.drawcoastlines(color='gray')
m.drawcountries(color='black')
m.drawstates(color='gray')
m.etopo(scale=0.2, alpha=0.3)
lat = gp.get_group('NO2') ['Latitud'].values
lon = gp.get_group('NO2') ['Longitud'].values
maximos = gp.get_group('NO2') ['Máximo'].values
area = gp.get_group('NO2') ['Máximo'].values
plotter = m.scatter(lon, lat, latlon=True,
          c=maximos, s=area,
          cmap='viridis', alpha=2)
cb = fig.colorbar(plotter, ax=ax)

# Mapa 4
ax = fig.add_subplot(3,3,4)
ax.set_title('O3')
m = Basemap(
    ax = ax,
    resolution = 'i',
    projection = 'merc',
    llcrnrlon = -79, llcrnrlat = -5,
    urcrnrlon = -65.537390, urcrnrlat = 11.934540 
)
m.drawcoastlines(color='gray')
m.drawcountries(color='black')
m.drawstates(color='gray')
m.etopo(scale=0.2, alpha=0.3)
lat = gp.get_group('O3') ['Latitud'].values
lon = gp.get_group('O3') ['Longitud'].values
maximos = gp.get_group('O3') ['Máximo'].values
area = gp.get_group('O3') ['Máximo'].values
plotter = m.scatter(lon, lat, latlon=True,
          c=maximos, s=area,
          cmap='viridis', alpha=2)
cb = fig.colorbar(plotter, ax=ax)

# Mapa 5
ax = fig.add_subplot(3,3,5)
ax.set_title('PM10')
m = Basemap(
    ax = ax,
    resolution = 'i',
    projection = 'merc',
    llcrnrlon = -79, llcrnrlat = -5,
    urcrnrlon = -65.537390, urcrnrlat = 11.934540 
)
m.drawcoastlines(color='gray')
m.drawcountries(color='black')
m.drawstates(color='gray')
m.etopo(scale=0.2, alpha=0.3)
lat = gp.get_group('PM10') ['Latitud'].values
lon = gp.get_group('PM10') ['Longitud'].values
maximos = gp.get_group('PM10') ['Máximo'].values
area = gp.get_group('PM10') ['Máximo'].values
plotter = m.scatter(lon, lat, latlon=True,
          c=maximos, s=area,
          cmap='viridis', alpha=2)
cb = fig.colorbar(plotter, ax=ax)
# Mapa 6
ax = fig.add_subplot(3,3,6)
ax.set_title('PM2.5')
m = Basemap(
    ax = ax,
    resolution = 'i',
    projection = 'merc',
    llcrnrlon = -79, llcrnrlat = -5,
    urcrnrlon = -65.537390, urcrnrlat = 11.934540 
)
m.drawcoastlines(color='gray')
m.drawcountries(color='black')
m.drawstates(color='gray')
m.etopo(scale=0.2, alpha=0.3)
lat = gp.get_group('PM2.5') ['Latitud'].values
lon = gp.get_group('PM2.5') ['Longitud'].values
maximos = gp.get_group('PM2.5') ['Máximo'].values
area = gp.get_group('PM2.5') ['Máximo'].values
plotter = m.scatter(lon, lat, latlon=True,
          c=maximos, s=area,
          cmap='viridis', alpha=2)
cb = fig.colorbar(plotter, ax=ax)
# Mapa 5
ax = fig.add_subplot(3,3,7)
ax.set_title('PST')
m = Basemap(
    ax = ax,
    resolution = 'i',
    projection = 'merc',
    llcrnrlon = -79, llcrnrlat = -5,
    urcrnrlon = -65.537390, urcrnrlat = 11.934540 
)
m.drawcoastlines(color='gray')
m.drawcountries(color='black')
m.drawstates(color='gray')
m.etopo(scale=0.2, alpha=0.3)
lat = gp.get_group('PST') ['Latitud'].values
lon = gp.get_group('PST') ['Longitud'].values
maximos = gp.get_group('PST') ['Máximo'].values
area = gp.get_group('PST') ['Máximo'].values
plotter = m.scatter(lon, lat, latlon=True,
          c=maximos, s=area,
          cmap='viridis', alpha=2)
cb = fig.colorbar(plotter, ax=ax)



ax = fig.add_subplot(3,3,8)
ax.set_title('SO2')
m = Basemap(
    ax = ax,
    resolution = 'i',
    projection = 'merc',
    llcrnrlon = -79, llcrnrlat = -5,
    urcrnrlon = -65.537390, urcrnrlat = 11.934540 
)
m.drawcoastlines(color='gray')
m.drawcountries(color='black')
m.drawstates(color='gray')
m.etopo(scale=0.2, alpha=0.3)
lat = gp.get_group('SO2') ['Latitud'].values
lon = gp.get_group('SO2') ['Longitud'].values
maximos = gp.get_group('SO2') ['Máximo'].values
area = gp.get_group('SO2') ['Máximo'].values
plotter = m.scatter(lon, lat, latlon=True,
          c=maximos, s=area,
          cmap='viridis', alpha=2)
cb = fig.colorbar(plotter, ax=ax)

#total plot

lat = df['Latitud'].values
lon = df['Longitud'].values
maximos = df['Máximo'].values
area = df['Máximo'].values

# Habilitamos la figura y establecemos ejes y título
ax = fig.add_subplot(3,3,9)
ax.set_title('Todos los gases')
# Establecemos la proyección del mapa base
m = Basemap(
    ax = ax,
    resolution = 'i',
    projection = 'merc',
    llcrnrlon = -79, llcrnrlat = -5,
    urcrnrlon = -65.537390, urcrnrlat = 11.934540 
)
 
# Establecemos las capas vectoriales a cargar como mapa base
m.drawcoastlines(color='gray')
m.drawcountries(color='black')
m.drawstates(color='gray')
m.etopo(scale=0.2, alpha=0.3)

plt.figure(0)

plotter = m.scatter(lon, lat, latlon=True,
          c=maximos, s=area,
          cmap='viridis', alpha=2)

cb = fig.colorbar(plotter, ax=ax)

fig.savefig('/content/gdrive/My Drive/Colab Notebooks/folium/to.png')
plt.show()
