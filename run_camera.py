import numpy as np
import cv2
from core import *

roi_sx = 170
roi_sy = 40
roi_ex = 470
roi_ey = 440

train, train_labs, train_code = traverse_dir("./data/mltest/")
#print(train_labs)
train = np.array(train)
_, trainX, trainY = train.shape
train = train.reshape(-1, trainX * trainY).astype(np.float32)

train_labs = np.array(train_labs)
train_labs = train_labs[:, np.newaxis]

# train model use OpenCV K-Nearest Neighbour
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labs)

#USB camra
cap = cv2.VideoCapture(1)
#IP Camra
#cap = cv2.VideoCapture("http://<username>:<password>@192.168.1.201:8088/video.cgi?.mjpg")

while True:
	ret,frame = cap.read()
	image = image_proc(frame)
	image = image.reshape(-1, trainX * trainY).astype(np.float32)

	# run knn model test
	ret, result, neighbour, dist = knn.findNearest(image, k=5)
	print(train_code[int(result)])

	#ROI area
	cv2.rectangle(frame,(roi_sx,roi_sy),(roi_ex,roi_ey),(0,0,255),3)
	#tip
	cv2.putText(frame, "type 's' to save ROI image & 'ESC' to exist", (10,20), 0, 0.5, (255,0,0), 2, cv2.LINE_AA)

	#show frame
	cv2.imshow("frame", frame)
	#cv2.imshow("ROI", roi_guss)

	# type "s" to save ROI image & "ESC" to exist
	k = cv2.waitKey(500) & 0xFF
	if (k == 27):
		break