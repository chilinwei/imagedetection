import numpy as np
import cv2
from datetime import datetime

roi_sx = 170
roi_sy = 40
roi_ex = 470
roi_ey = 440


#USB camra
cap = cv2.VideoCapture(1)
#IP Camra
#cap = cv2.VideoCapture("http://admin:1234@192.168.1.201:8088/video.cgi?.mjpg")

while True:
	t = datetime.now()
	s = t.second
	fn = datetime.strftime(t, '%Y%m%d%H%M%S%U')

	ret,frame1 = cap.read()
	frame2 = frame1

	#get ROI area
	roi = frame2[roi_sy:roi_ey, roi_sx:roi_ex]


	#draw frame
	#ROI area
	#cv2.rectangle(frame1,(roi_sx,roi_sy),(roi_ex,roi_ey),(0,0,255),3)
	#tip
	cv2.putText(frame1, "type 's' to save ROI image & 'ESC' to exist", (10,20), 0, 0.5, (255,0,0), 2, cv2.LINE_AA)

	#show frame
	cv2.imshow("frame1", frame1)
	cv2.imshow("ROI", roi)


	k = cv2.waitKey(5) & 0xFF

	if (k == 27):
		break

	elif k == ord("s"):
		cv2.imwrite("data/uncategorized/"+fn+".jpg", roi)