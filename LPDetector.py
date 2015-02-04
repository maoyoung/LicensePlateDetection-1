""""

Michelle Sit
Spring 2015
MIT Sensible Lab UROP

"""


import scipy
import numpy
import cv2
import sys


#video_capture = cv2.VideoCapture('./MA_plate.jpg') #Will be used for video capture
video_capture = cv2.imread('IMG_0378.jpg')

while True:
	#ret, frame = video_capture.read() # will be used for video capture



	#displays frames
	#cv2.imshow('Video', frame)
	cv2.imshow('picture', video_capture)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

video_capture.release()
cv2.destroyAllWindows()