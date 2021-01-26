import cv2
import os
import time

total_count = 100
length = 50
more = "Y"
root_path = os.path.abspath(os.path.dirname(__file__))
if not os.path.isdir(os.path.join(root_path, "Image")):
    os.mkdir(os.path.join(root_path, "Image"))

while more.lower() == "y":
    name = input("Name pls!\ntype your name: ")
    data_path = os.path.join(root_path, "Image", name)

    if os.path.isdir(data_path):
        print("Already have data!")
    else:
        os.mkdir(data_path)
        camera = cv2.VideoCapture(0)
        face_model = cv2.CascadeClassifier(
            os.path.join(root_path, "haarcascades", "haarcascade_frontalface_alt2.xml"))
        count = 0
        print("collecting data ...")
        print("might need a few minutes ...")
        print("[>" + " " * length + "]", "0%", end="")
        while count < total_count:
            ret, frame = camera.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_model.detectMultiScale(
                gray, scaleFactor=1.5, minNeighbors=5)

            for (x, y, w, h) in faces:
                if (x, y, w, h) != (0, 0, 0, 0):
                    cv2.imwrite(os.path.join(
                        data_path, f"{count}.jpg"), frame[y:y+h, x:x+w])
                    count += 1
                    percent = count / total_count
                    num = int(length * percent)
                    print("\r[" + "=" * num + ">" + " " * (length - num) + "]",
                          f"{percent * 100:.1f}%", end="")

            time.sleep(0.001)

        camera.release()

    print("\r[" + "=" * length + "=]", "100.0%")
    print(f"{name} data collected!")
    more = input("Is there more people? [Y/n]: ")
