# import the necessary packages
import numpy as np
import pyautogui
import imutils
import cv2

image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
cv2.imwrite("in_memory_to_disk.png", image)
pyautogui.screenshot("straight_to_disk.png")

#we can then load our screenshot from disk in OpenCV format
image = cv2.imread("straight_to_disk.png")
cv2.imshow("Screenshot", imutils.resize(image, width=600))
cv2.waitKey(0)
