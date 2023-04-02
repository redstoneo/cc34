import numpy as np
import cv2


black=np.zeros([600,600])
#print(black)
#frow=black[:,1:2]
#print(frow)
black[200:400,200:400]=130
print(black)
cv2.imshow("black",black)
cv2.waitKey(0)

