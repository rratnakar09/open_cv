import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("dataset/lena.jpg")
'''
# pyramid transformation
lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)
lr3 = cv2.pyrDown(lr2)
hr2 = cv2.pyrUp(lr2)

cv2.imshow("original image", img)
cv2.imshow("pyrdown 1 image", lr1)
cv2.imshow("pyrdown 2 image", lr2)
cv2.imshow("pyrdown 3 image", lr3)
cv2.imshow("pyrUp 1 image", hr2)
'''

layer = img.copy()
# create a gaussian pyramid
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i), layer)

layer = gp[5]
cv2.imshow('upper level gp', layer)
lp = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()
