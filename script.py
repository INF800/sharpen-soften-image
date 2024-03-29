import cv2
import numpy as np

# sharpening blurry image
inim = cv2.imread('inim.png')
kernel = np.array([[-0.5,-0.5,-0.5], [-0.5,5,-0.5], [-0.5,-0.5,-0.5]])
im = cv2.filter2D(inim, -1, kernel)
cv2.imwrite('sharpim.png', im)

# softening sharpened Image
sharpim = cv2.imread('sharpim.png')
kernel = np.ones((3,3),np.float32)/9
softim = cv2.filter2D(sharpim, -1, kernel)
cv2.imwrite('ouput.png', softim)