# Detecting cats in images with OpenCV
# I will used pre-trained Haar classifiers to detect cats
# We have to keep changing scalefactor to detect the cat faces in all four cat images available in data folder


# Load the libraries
import cv2
from matplotlib import pyplot as plt

# Load the haar classifiers to detect cat face
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalcatface_extended.xml')

# read and display the image
# chnage the cat image name to say cat_02.jpg or cat_03.jpg or cat_04.jpg
img = cv2.imread('dataset/cat_01.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(img)
plt.title('image')
plt.xticks([])
plt.yticks([])
plt.show()

# returns the position of the detected faces as Rect(x,y,w,h),
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1,
                                      minNeighbors=1, minSize=(75, 75))

'''
print('Faces found: ', len(faces))
print('The image height, width, and channel: ',img.shape)
print('The coordinates of each face detected: ', faces)
'''

# Draw a green rectangle around the faces detected with a thickness of ‘2’
for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Show the new image with the rectangles highlighting the detected face.
plt.imshow(img)
plt.title('image')
plt.xticks([])
plt.yticks([])
plt.show()
