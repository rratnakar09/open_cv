# we will change the BGR value using a trackbar
import numpy as np
import cv2 as cv

'''
def nothing(x):
    # x is the value of current position of trackbar
    print(x)


# create a black image, a window
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

# create a trackbar which will change B channel
cv2.createTrackbar('B', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('R', 'image', 0, 255, nothing)

# create a switch trackbar
switch = '0: OFF\n 1:ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while (1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get the initial trackbar values
    b = cv2.getTrackbarPos('B', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    r = cv2.getTrackbarPos('R', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    # use switch to control the BGR trackbar
    if s == 0:
        img[:] = 0  # nothing will change in image
    else:
        img[:] = [b, g, r]

cv2.destroyAllWindows()

'''


def nothing(x):
    print(x)


# Create a black image, a window
cv.namedWindow('image')

cv.createTrackbar('CP', 'image', 10, 400, nothing)

switch = 'color/gray'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while (1):
    img = cv.imread('lena.jpg')
    pos = cv.getTrackbarPos('CP', 'image')
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (50, 150), font, 6, (0, 0, 255), 10)

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    img = cv.imshow('image', img)

cv.destroyAllWindows()
