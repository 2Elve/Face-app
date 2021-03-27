import cv2
import os
import imutils
import numpy as np 


personName = input("Enter the person's name: ")
dataPath = os.path.dirname(os.path.abspath(__file__)) + '/Data'
personPath = dataPath + '/' + personName 

if not os.path.exists(personPath):
	print('New Directory Created: ', personPath)
	os.makedirs(personPath)

cap = cv2.VideoCapture(0)
face_classif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count = 0

while True: 
	_,frame = cap.read()
	if _ == False: break 
	frame = imutils.resize(frame, width=640)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	auxFrame = frame.copy()

	faces = face_classif.detectMultiScale(gray,
		scaleFactor = 1.1,
		minNeighbors=8,
		minSize=(70,70),
		maxSize=(250,250))

	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,50),2)
		f = auxFrame[y:y+h,x:x+w]
		f = cv2.resize(f, (150,150), interpolation=cv2.INTER_CUBIC)
		cv2.imwrite(personPath + '/rostro_{}.jpg'.format(count),f)
		count = count + 1
		print('Count: {}'.format(count))

	cv2.imshow('Reading Face', frame)

	if cv2.waitKey(1) == 27 or count >= 500:
		break 

cap.release()
cv2.destroyAllWindows()