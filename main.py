import cv2
import matplotlib.pyplot as plt #preview the image
import numpy as np #for image rotation
#read the image
img=cv2.imread("image.png")
#convert the image into RGB
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#display the rgb image
plt.imshow(img_rgb)
plt.title("RGB Image")
plt.show()
#convert to grayscale
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale image",gray_img)#cv2 display format
cv2.waitKey(0)#keep the window open
#crop the rgb image
cropping_region=img_rgb[100:250,200:350]
plt.imshow(cropping_region)
plt.title("Cropped Image")
plt.show()
#rotate the image
(h,w)=img.shape[:2]#gets you the image properties
#define the center of rotation
center=(w//2,h//2)
rotation=cv2.getRotationMatrix2D(center,60,1.0)#60=degrees,1.0=rotating the whole image
#rotate the image based on rotation
rotated_img=cv2.warpAffine(img_rgb,rotation,(w,h))#ensures the entire image is rotated
cv2.imshow("Rotated Image",rotated_img)
cv2.waitKey(0)
#Brightness Control
brightness_matrix=np.ones(img.shape,dtype="uint8")*50 #50=brightness level
brighter_img=cv2.add(img_rgb,brightness_matrix)#increase the brightness
darker_img=cv2.subtract(img_rgb,brightness_matrix)#decrease the brightness
cv2.imshow("Brighter Image",brighter_img)
cv2.imshow("Darker image", darker_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
