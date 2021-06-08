# -*- coding: utf-8 -*-
"""HW3function.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yLUdSnQpRFeiVRWzjNsS57cklVHJZRMH
"""

#Installations
!apt install gdal-bin python-gdal python3-gdal 
!pip install rasterio
!apt install python3-rtree 
!pip install git+git://github.com/geopandas/geopandas.git
!pip install descartes

import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import rasterio as rio
from rasterio.plot import show

from google.colab import drive

drive.mount('/content/drive', force_remount = True)

fpath='/content/drive/My Drive/muldrow_20210311.tif'

def rasterio_open(f):

  """ 
  This function opens the input image using raster data which can
  will use the rasterio package to bring GDAL-supported data formats
  into our python session as numpy arrays.

  Parameters
  ----------
  fpath: path of the image
  path of the raster data can be from any source, in our case it's from AWS
  it wil transform image and 

  Returns
  ----------
  shape,ESPG,driver, dtype,units

  Examples
  ----------
  >>>src_image = rasterio_open(fpath)
  Make tiff gdal functions compatible

  >>>print(src_image.profile)
  displays information of the tif

  """
  return rio.open(f)

src_image = rasterio_open(fpath)
print(src_image.profile)

fig, ax = plt.subplots(1, figsize=(12, 10))
show(src_image, ax=ax,cmap='gray')
plt.show()

def elev_map():
    transform = src_image.meta['transform']
    array2011 = src_image.read(1, masked=True)
    transform_affine=transform.to_gdal()
    array2011_chop = array2011[5:-5,5:-5]
    plt.imshow(array2011_chop, interpolation='nearest', vmin=-3.4,vmax=3.4, cmap='gray')
    plt.colorbar()
    plt.title('Elevation Change Map')

    """ 
  This function opens the input image using raster data which can
  will use the rasterio package to bring GDAL-supported data formats
  into our python session as numpy arrays.

  Parameters
  ----------
  array2011: Rasterio opened and transformed image 

  Returns
  ----------
  Elevation Change Rate Map

  Examples
  ----------
  >>>plt.imshow(array2011_chop, interpolation='nearest', vmin=-3.4,vmax=3.4, cmap='gray')
  Slope change map displays


  """

fig, ax = plt.subplots(1, figsize=(8, 6))
elev_map()
