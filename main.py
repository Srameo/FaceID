import os
import sys
import time

root_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(root_path)

from face_detector import FaceDetector
import cv2
import pyautogui
import json

time_limit = 10.0
face = FaceDetector()
font = cv2.FONT_HERSHEY_PLAIN
detector = cv2.face.LBPHFaceRecognizer_create()  # detector for trec or recognizer
# Use the full path of your trained.yml file. This file contains the weights for your face
detector.read(f'{root_path}/Model/trained_LBPH.yml')

vid = cv2.VideoCapture(0)

# Use the full path of your lable.pickle file. This file contains the name of recognized users
with open(f'{root_path}/Model/label.json', 'r') as f:
    labels = {a: b for b, a in json.load(f).items()}

start_time = time.time()
while (vid.isOpened()):
    _, frame = vid.read()
    frame = cv2.flip(frame, 1)
    img, roi, x, y = face.detect(frame)

    if time.time() - start_time > time_limit:
        break

    if roi is not None:
        idd, conf = detector.predict(roi)

        if conf >= 0.8:
            # Enter the name as in label.json file, for which the computer should log in
            if labels[idd] == "srameo":
                pyautogui.click()
                pyautogui.write('JinSr@meo0217')   # Enter you password here
                pyautogui.press('enter')
                # Ask it to say whatever you want when user logs in
                os.system("echo welcome srameo!")
                break
            else:
                # Ask it to say whatever you want when someone else logs in
                os.system("echo eat shit")
        else:
            # Ask it to say whatever you want when someone else logs in
            os.system("echo eat shit")
            #cv2.putText(img,labels[idd],(x,y + 20),font,1,(0,255,0),2)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

print(f"spend time: {time.time() - start_time}")
vid.release()