# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 22:22:28 2022

@author: kavin
"""

from skimage import io,filters,color
from matplotlib import pyplot as plt
import cv2
img = io.imread("images/luffy.jpg")
print(img)
plt.hist(img.flat,bins=256,range=(0, 100))
plt.show()
# x = color.rgb2gray(img)
# cv2.imshow("image",x)
# cv2.waitKey(0)

# gaussian_img = filters.gaussian(img,sigma=1)
# plt.imshow(gaussian_img)
