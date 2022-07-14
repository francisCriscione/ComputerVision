import numpy as np
import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/cv2/data/haarcascade_eye.xml')

fgbg = cv2.createBackgroundSubtractorMOG()

while (True):
    #capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame', gray)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

     #returns a list of rectangles




cap.release()
cv2.destroyAllWindows()
