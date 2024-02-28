import cv2
import numpy as np

video=cv2.VideoCapture(0)

while True:
  ret, frame=video.read()

  gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

  edges=cv2.Canny(gray,90,170)

  edges_cvt=cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)

  combined=np.hstack((frame,edges_cvt))

  cv2.imshow('Video , Edges',combined)

  if cv2.waitKey(1) == ord('q'):
    break

video.release()
cv2.destroyAllWindows()
