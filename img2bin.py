# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 22:21:48 2022

@author: kavin
"""

import numpy as np
import random
import cv2
from matplotlib import pyplot as plt

from skimage import io

img=io.imread('images/a_bin.tif',as_gray=False)
(thresh, im_bw) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
thresh = 127
im_bw = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite('bw_image.png', im_bw)