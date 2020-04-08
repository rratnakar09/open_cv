# Adaptive Thresholding
# calculates threshold for a smaller region of an image so that we can get different threshold
# for different region of the image

import cv2


img = cv2.imread('sudoku.png', 0)
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# threshold value is the mean of neighbourhood area.
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
# threshold value is the weighted sum of neighbourhood values where weights are a gaussian window
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)


cv2.imshow('image', img)
cv2.imshow('th1', th1)
cv2.imshow('th2', th2)
cv2.imshow('th3', th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
exit()
