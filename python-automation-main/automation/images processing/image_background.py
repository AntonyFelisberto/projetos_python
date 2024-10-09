import cv2
import numpy as np

foreground = cv2.imread("backs/giraffe.jpeg")
background = cv2.imread("backs/safari.jpeg")

print(foreground[40,40])
width = foreground.shape[1]
height = foreground.shape[0]
print(foreground.shape)

resized_backgorund = cv2.resize(background, (width, height))

for i in range(width):
    for j in range(height):
        pixel = foreground[j, i]    #pixel will be a numpy array
        if np.any(pixel == [1,255,0]): #green pixel, np.any check if pixel has any value similar to the specified
            foreground[j, i] = resized_backgorund[j, i]

cv2.imwrite("output.jpeg",foreground)