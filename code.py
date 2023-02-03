import cv2
import numpy as np

img=cv2.imread("PRO-104-Project-Image-main/PRO-104-Project-Image-main/solar-system.jpg")
# cv2.imshow('output',img)
cv2.putText(img,'sun',(20,225),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
cv2.putText(img,'mercury',(110,200),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'venus',(190,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'earth',(290,150),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'mars',(380,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'jupiter',(500,100),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'saturn',(800,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'neptune',(950,150),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'uranus',(1115,270),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.imwrite('Solar_systemwithname.jpg',img)
cv2.imshow("helo",img)
cv2.waitKey(0)