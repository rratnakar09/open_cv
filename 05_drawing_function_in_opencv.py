# drawing a line on an image

import cv2


img = cv2.imread('lena.jpg')

img = cv2.line(img, (0,0), (255,255), (0,255,0), 10)
img = cv2.arrowedLine(img, (0,255), (255,255), (0,135,0), 10)

# draw a rectangle
img = cv2.rectangle(img, (384,0), (518,128), (0,0,255), 10)

# draw a circle
img = cv2.circle(img, (447,63), 63, (0,255,0), -1)

# write some text on image
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCV', (10,500), font, 4, (255,255,255), 10, cv2.LINE_AA)


cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()