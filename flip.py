# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 23:43:02 2022

@author: kavin
"""
import numpy as np
import random
import cv2
from matplotlib import pyplot as plt

from skimage import io


img = cv2.imread('images/luffy.jpg')

imageV = cv2.flip(img, 0)
imageH = cv2.flip(img, 1)
plt.rcParams["figure.figsize"] = [10.00, 6.50]
plt.rcParams["figure.autolayout"] = True
plt.subplot(1, 2, 1)
plt.imshow(imageV)

plt.subplot(1, 2, 2)
plt.imshow(imageH)


plt.show()