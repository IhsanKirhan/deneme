import cv2

cap=cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()
    
    if not ret:
        break
    
    cv2.imshow("pencere", frame)
    
    if cv2.waitKey(20) & 0xFF==ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(2)
    