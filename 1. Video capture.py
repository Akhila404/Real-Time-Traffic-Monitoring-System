import cv2
from tracker import* #tracking contain 8 tracking algo

cap = cv2.VideoCapture("highway.mp4")            #path of your video

while True:
    ret, frame = cap.read()
    
    cv2.imshow('Frame', frame)
    
    key = cv2.waitKey(30)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
