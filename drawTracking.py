import cv2
import time
cap = cv2.VideoCapture(0)
time.sleep(1)
tracker = cv2.TrackerMOSSE_create()


success, img = cap.read()
boundingBox = cv2.selectROI("Tracking", img, False)
tracker.init(img, boundingBox)

def drawBox(img, boundingBox):
    x, y, w, h = int(boundingBox[0]), int(boundingBox[1]), int(boundingBox[2]), int(boundingBox[3])
    print(x,y,w,h)
    cv2.rectangle(img, (x,y), ((x+w), (y+h)), (255, 0, 255), 3, 1)


while (True):
    timer = cv2.getTickCount()
    success, img = cap.read()


    success, boundingBox = tracker.update(img)

    if success:
        drawBox(img, boundingBox)
    else:
        break


    FPS = cv2.getTickFrequency()/(cv2.getTickCount() - timer)
    cv2.putText(img, str(int(FPS)), (75, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow('Tracking', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
