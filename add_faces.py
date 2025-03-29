import cv2
import numpy as np
import pickle
import os

if not os.path.exists('data'):
    os.makedirs('data')

video = cv2.VideoCapture(0)
facedetect= cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

faces_data = []
i=0

name = input("Enter your name: ")
while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        crop = frame[y:y+h, x:x+w, :]
        resized_img = cv2.resize(crop, (50, 50))
        if len(faces_data)<=100 and i%10==0:
            faces_data.append(resized_img)
        i=i+1
        cv2.putText(frame,str(len(faces_data)),(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
    cv2.imshow('Video', frame)
    k = cv2.waitKey(1)
    if k==ord('q') or len(faces_data)==100:
        break
video.release()
cv2.destroyAllWindows()

# ...existing code... (keep everything until line 35)

faces_data = np.array(faces_data)
faces_data = faces_data.reshape(100, -1)

# Create names list for the current person
names = [name]*100

# Fix the names.pkl file handling
if 'names.pkl' not in os.listdir('data/'):
    # If file doesn't exist, create new file with current names
    with open('data/names.pkl', 'wb') as f:
        pickle.dump(names, f)
else:
    # If file exists, append new names to existing ones
    with open('data/names.pkl', 'rb') as f:
        existing_names = pickle.load(f)
    names = existing_names + names
    with open('data/names.pkl', 'wb') as f:
        pickle.dump(names, f)

# Fix the faces_data.pkl file handling
if 'faces_data.pkl' not in os.listdir('data/'):
    # If file doesn't exist, create new file with current faces_data
    with open('data/faces_data.pkl', 'wb') as f:
        pickle.dump(faces_data, f)
else:
    # If file exists, append new faces_data to existing ones
    with open('data/faces_data.pkl', 'rb') as f:
        faces = pickle.load(f)
    faces = np.append(faces, faces_data, axis=0)
    with open('data/faces_data.pkl', 'wb') as f:
        pickle.dump(faces, f)