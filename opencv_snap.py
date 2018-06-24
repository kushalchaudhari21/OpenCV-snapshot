import cv2

_,frame = cap.read()

gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
mypath = "/Users/Documents/workspace/work/opencv/test/data/"
cv2.imwrite((mypath + 'captured.jpg'), gray)




cv2.destroyAllWindows()
cap.release()
