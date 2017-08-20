from core import *
import cv2
import numpy as np

IMAGE_SIZE = 100


cap = cv2.VideoCapture(1)

while True:
	ret,frame = cap.read()



	img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	img = cv2.resize(img, (IMAGE_SIZE, IMAGE_SIZE))
	img = cv2.medianBlur(img,5)
	img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)

	kernel1 = np.ones((1,1),np.uint8)
	img = cv2.dilate(img,kernel1,iterations = 1)
	
	#img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
	kernel2 = np.ones((1,1),np.uint8)
	img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel2)

	cv2.imshow("frame", img)


	k = cv2.waitKey(500) & 0xFF
	if (k == 27):
		break

#img = cv2.imread("data/hand1.jpg")
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##ret,img = cv2.threshold(img,0,255,cv2.THRESH_BINARY)
#img = cv2.medianBlur(img,5)
#img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
#cv2.imshow("image",img)
#cv2.waitKey(10000)