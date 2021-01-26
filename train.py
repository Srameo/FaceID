import json
import os
import cv2
import numpy as np

root_path = os.path.abspath(os.path.dirname(__file__))
img_dir = os.path.join(root_path, "Image")
model_dir = os.path.join(root_path, "Model")
if not os.path.isdir(model_dir):
    os.mkdir(model_dir)

rec = cv2.face.LBPHFaceRecognizer_create()
all_ids = 0
label2id = {}

face_model = cv2.CascadeClassifier(
    os.path.join(root_path, "haarcascades", "haarcascade_frontalface_alt2.xml"))

x_train = []
y_train = []

for root, dirs, files in os.walk(img_dir):
    for file in files:
        if file.endswith('png') or file.endswith('jpg'):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(" ","-").lower()
            
            if not label in label2id:
                label2id[label] = all_ids
                all_ids += 1
 
 
            id_ = label2id[label]  
 
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) #converts to gray scale
 
            x_train.append(img)
            y_train.append(id_)     
 
 
with open(f'{model_dir}/label.json', 'w') as f:
    json.dump(label2id, f)

rec.train(x_train, np.array(y_train))
rec.save(f"{model_dir}/trained.yml")
