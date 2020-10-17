import cv2

cap = cv2.VideoCapture(0)
cascade_classifier = cv2.CascadeClassifier('haarcascades\haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()

    cv2.imshow('frame',frame)

    cv2.waitKey(1)
