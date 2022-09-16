# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 19:41:44 2022

@author: kavin
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("images/foredge.tif")
img = cv2.GaussianBlur(img, (3,3), 0) 

sobelx = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) 
# Sobel Edge Detection on the X axis 
sobely = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) 
# Sobel Edge Detection on the Y axis
sobelxy = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) 
# Combined X and Y Sobel Edge Detection
   
# Display Sobel Edge Detection Images   
# cv2.imshow('Sobel X', sobelx)   

# cv2.imshow('Sobel Y', sobely)

# cv2.imshow('Sobel X Y using Sobel() function', sobelxy)


#prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img, -1, kernelx)
img_prewitty = cv2.filter2D(img, -1, kernely)





cv2.imshow("Prewitt X", img_prewittx)
cv2.imshow("Prewitt Y", img_prewitty)
cv2.imshow("Prewitt", img_prewittx + img_prewitty)

cv2.waitKey(0)
cv2.destroyAllWindows()