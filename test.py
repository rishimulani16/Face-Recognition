from sklearn.neighbors import KNeighborsClassifier

import cv2
import numpy as np
import pickle
import os

if not os.path.exists('data'):
    os.makedirs('data')

video = cv2.VideoCapture(0)
facedetect= cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

with open('data/names.pkl', 'rb') as f:
        LABLES = pickle.load(f)

with open('data/faces_data.pkl', 'rb') as f:
        FACES = pickle.load(f)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABLES)


while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        crop = frame[y:y+h, x:x+w, :]
        resized_img = cv2.resize(crop, (50, 50)).flatten().reshape(1, -1)
        output = knn.predict(resized_img)
        cv2.putText(frame, output[0], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
    cv2.imshow('Video', frame)
    k = cv2.waitKey(1)
    if k==ord('q') :
        break
video.release()
cv2.destroyAllWindows()

