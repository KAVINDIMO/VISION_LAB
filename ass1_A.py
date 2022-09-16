# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 21:36:29 2022

@author: kavin
"""

import numpy as np
import random
import cv2
from matplotlib import pyplot as plt

from skimage import io

img1= cv2.imread('bw_image.png')
img2 = cv2.imread('images/a_bin.tif')
img3 = cv2.imread('images/luffy.jpg')
plt.rcParams["figure.figsize"] = [10.00, 6.50]
plt.rcParams["figure.autolayout"] = True

plt.subplot(1, 3, 1)
plt.imshow(img1)
plt.title("First")

plt.subplot(1, 3, 2)
plt.imshow(img2)
plt.title("Second")

plt.subplot(1, 3, 3)
plt.imshow(img3)
plt.title("Third")


plt.show()





