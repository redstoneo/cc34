import cv2

img=cv2.imread("OIP.jpg")
cv2.imshow("display",img)
#print(img)
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("gray",gray)
print(gray)
cv2.waitKey(0)
