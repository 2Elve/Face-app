import cv2
import os

def face_id():

	dataPath = os.path.dirname(os.path.abspath(__file__)) + '/Data'
	imagePaths = os.listdir(dataPath)
	print('Image Paths: ',imagePaths)

	face_recognizer = cv2.face.EigenFaceRecognizer_create()
	face_recognizer.read('Models/modelEigen.xml')

	cap = cv2.VideoCapture(0)

	faceClassif = cv2.cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

	for i in range(200):

		_,frame = cap.read()
		if _ == False: break
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		auxFrame= gray.copy()

		faces = faceClassif.detectMultiScale(gray,
			scaleFactor = 1.1,
			minNeighbors=8,
			minSize=(70,70),
			maxSize=(250,250))

		for (x,y,w,h) in faces: 
			f = auxFrame[y:y+h,x:x+h]
			f = cv2.resize(f,(150,150), interpolation=cv2.INTER_CUBIC)
			result = face_recognizer.predict(f)

			cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)

			if result[1]<8700:
				cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(255,252,238),1,cv2.LINE_AA)
				cv2.rectangle(frame, (x,y), (x+w,y+h), (255,252,238),1)
			else:
				cv2.putText(frame,'Unknown',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
				cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255),2)

		cv2.imshow('Facial Recognizer',frame)

		if cv2.waitKey(1) == 27:
			break 

	cap.release()
	cv2.destroyAllWindows()
	return result[0]