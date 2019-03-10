Before run :
sudo modprobe bcm2835-v4l2 

Install Packages :

pip install dlib
pip install face_recognition
pip install inutile
pip install pillow

custom dataset -> run pip install --upgrade imutils

run :

encode_faces.py -> python encode_faces.py --dataset dataset --encodings encodings.pickle \
	--detection-method hog

pi_face_recognition -> python pi_face_recognition.py --cascade haarcascade_frontalface_default.xml \
	--encodings encodings.pickle

dataset custom - > python build_face_dataset.py --cascade haarcascade_frontalface_default.xml \
	--output dataset/irwan

Test Camera : raspistill -o cam.jpg
