import cv2
import numpy as np

img = cv2.imread('C:/Users/mayanxoni/PycharmProjects/openCVTest/img/tom.jpg')

cv2.imshow('Tom Cruise', img)
cv2.waitKey(0)

# returnValue, blackAndWhite = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# cv2.imshow("Black & White", blackAndWhite)
# cv2.waitKey(0)

img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# cv2.imshow("HSV Image", img_HSV)
# cv2.waitKey(0)
# cv2.imshow("Hue Image", img_HSV[:, :, 0])
# cv2.waitKey(0)
# cv2.imshow("Saturation Image", img_HSV[:, :, 1])
# cv2.waitKey(0)
# cv2.imshow("Value Image", img_HSV[:, :, 2])
# cv2.waitKey(0)

B, G, R = cv2.split(img)
cv2.waitKey(0)
zeros = np.zeros(img.shape[:2], dtype="uint8")
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.waitKey(0)
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.waitKey(0)

cv2.destroyAllWindows()