import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("images/test01.jpg")

# print(img)

print(img.shape)

plt.imshow(img)
plt.show()