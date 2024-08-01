import cv2
import pickle
import numpy as np
import os

if not os.path.exists('data'):
    os.makedirs('data')

video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

faces_data = []
i = 0

name = input("Enter Your Name: ")

while True:
    ret, frame = video.read()
    if not ret:
        print("Failed to capture image")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w, :]
        resized_img = cv2.resize(crop_img, (50, 50))
        if len(faces_data) <= 100 and i % 10 == 0:
            faces_data.append(resized_img)
            print(f"Captured face {len(faces_data)}")
        i += 1
    if len(faces_data) >= 100:
        print("Collected 100 faces, stopping capture.")
        break

video.release()

faces_data = np.asarray(faces_data)
faces_data = faces_data.reshape(100, -1)

names_path = 'data/names.pkl'
faces_data_path = 'data/faces_data.pkl'

if not os.path.exists(names_path):
    names = [name] * 100
    with open(names_path, 'wb') as f:
        pickle.dump(names, f)
else:
    with open(names_path, 'rb') as f:
        names = pickle.load(f)
    names = names + [name] * 100
    with open(names_path, 'wb') as f:
        pickle.dump(names, f)

if not os.path.exists(faces_data_path):
    with open(faces_data_path, 'wb') as f:
        pickle.dump(faces_data, f)
else:
    with open(faces_data_path, 'rb') as f:
        faces = pickle.load(f)
    faces = np.append(faces, faces_data, axis=0)
    with open(faces_data_path, 'wb') as f:
        pickle.dump(faces, f)

print("Face data collection and saving complete.")
