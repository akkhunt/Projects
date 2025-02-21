import cv2,os
import numpy as np
from PIL import Image

recognizer = cv2.createLBPHFaceRecognizer()
detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
path='dataSet'
def getImagesWithID(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    print imagePaths
    faces=[]
    IDs=[]
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L')
        faceNp=np.array(faceImg,'uint8')
        ID=int(os.path.split(imagePath)[-1].split('.')[1])
        print ID
        faces.append(faceNp)
        IDs.append(ID)
        cv2.imshow("training",faceNp)
        cv2.waitKey(10)
    return faces,IDs

faces,Ids = getImagesWithID(path)
recognizer.train(faces, np.array(Ids))
recognizer.save('trainner/trainner.yml')

