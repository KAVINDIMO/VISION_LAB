# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 23:52:10 2022

@author: kavin


"""

import numpy as np
import random
import cv2
from matplotlib import pyplot as plt

from skimage import io


image = cv2.imread('images/luffy.jpg')

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), 90, 0.5)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("rotate 90 and scale down 0.5", rotated)

M = cv2.getRotationMatrix2D((cX, cY), 90, 2.5)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotate 90 and scale up 2.5", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()