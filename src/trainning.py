import cv2
import os 
import numpy as np 


dataPath = os.path.dirname(os.path.abspath(__file__)) + '/Data'
peopleList = os.listdir(dataPath)

labels = []
facesData = []
label = 0 

for nameDir in peopleList:
	personPath = dataPath + '/' + nameDir
	print('Reading Images')

	for fileName in os.listdir(personPath):
		print('Faces: ', nameDir + '/' + fileName)
		labels.append(label)
		facesData.append(cv2.imread(personPath+'/'+fileName,0))
		img = cv2.imread(personPath+'/'+fileName,0)
	label += 1

#face_recognizer = cv2.face.EigenFaceRecognizer_create()
face_recognizer = cv2.face.FisherFaceRecognizer_create()


#Trainning 
print('Trainning...')
face_recognizer.train(facesData,np.array(labels))

face_recognizer.write('modelFisher.xml')
print('Classifier Trainned uwu')