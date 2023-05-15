import cv2
import time
import math

video = cv2.VideoCapture("bb3.mp4")

check, img = video.read()

bbox = cv2.selectROI('Rastreando', img, False)

tracker = cv2.TrackerCSRT_create()

tracker.init(img, bbox)

print(bbox)


def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])

    cv2.rectangle(img, (x,y), ( (x+w), (y+h) ), (0,0,255), 3,)


while True:
    check, img = video.read() 

    sucesso, bbox = tracker.update(img)  

    if sucesso:
        drawBox(img, bbox)
    else:
        cv2.putText(img,'Objeto perdido', (75,90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

    cv2.imshow("resultado",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Interrompido!")
        break


video.release()
cv2.destroyALLwindows()