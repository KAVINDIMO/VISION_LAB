# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 19:00:40 2022

@author: kavin
"""

import cv2

from matplotlib import pyplot as plt

img = cv2.imread("images/luffy.jpg")

color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])


plt.show("hist",img)