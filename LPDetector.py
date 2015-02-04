""""

Michelle Sit
Spring 2015
MIT Sensible Lab UROP

"""

import scipy
import numpy as np
import cv2
import sys
import pdb
from copy import deepcopy

#video_capture = cv2.VideoCapture('./MA_plate.jpg') #Will be used for video capture
video_capture = cv2.imread('IMG_0378.jpg')

while True:
	#ret, frame = video_capture.rIMG_ead() # will be used for video apture
	frame = deepcopy(video_capture)
#	blur = cv2.GaussianBlur(video_capture, (7,7), 0)
	gray = cv2.cvtColor(video_capture, cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray, 150, 300, 3) #need to make these numbers proportional
	closing = cv2.morphologyEx (edges, cv2.MORPH_CLOSE, np.ones((5,5), np.uint8))
	#dilated = cv2.dilate (closing, np.ones((4,4), np.uint8), iterations = 1)

	#line detector
	lines = cv2.HoughLinesP(closing, 1, np.pi/2, 10, 10, 80)
	#lines = cv2.HoughLines(edges, 1, np.pi/180, 100, 0, 0)
	print lines

	#draw lines on image
	if lines != None:
		for (x1, y1, x2, y2) in lines[len(lines)-1]:
			cv2.line(video_capture, (x1, y1), (x2, y2), (255, 0, 0), 3, 2)

	# if lines != None:
	# 	for rho, theta in lines[0]:
	# 		    a = np.cos(theta)
	# 		    b = np.sin(theta)
	# 		    x0 = a*rho
	# 		    y0 = b*rho
	# 		    x1 = int(x0 + 1000*(-b))
	# 		    y1 = int(y0 + 1000*(a))
	# 		    x2 = int(x0 - 1000*(-b))
	# 		    y2 = int(y0 - 1000*(a))
	# 		    cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 3, 8)

	else:
		print "nothing found"

	#displays frames
	#cv2.imshow('Video', frame)
	#cv2.imshow('picture', video_capture)
	cv2.imshow('deepcopy', frame)
	cv2.imshow('dilated', closing)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

video_capture.release()
cv2.destroyAllWindows()