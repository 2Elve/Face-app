import numpy as np
import cv2

img = cv2.imread('Icons/Mystic.jpg',-1)
f = cv2.resize(img,(800,450), interpolation=cv2.INTER_CUBIC)
cv2.imshow('image',f)
print(f.shape)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('backb.png',f)
    cv2.destroyAllWindows()