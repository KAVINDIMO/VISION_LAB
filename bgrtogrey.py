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


img = cv2.imread('images/luffy.jpg')
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
plt.rcParams["figure.figsize"] = [10.00, 6.50]
plt.rcParams["figure.autolayout"] = True
plt.subplot(1, 2, 1)
plt.imshow(img)

plt.subplot(1, 2, 2)
plt.imshow(image_rgb)



plt.show()





