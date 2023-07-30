"""
This python file is used to introduce the images handling in python to the user.
"""
import cv2
import os

#import numpy as np

# Read the image 1 means read the image in color mode zero means read the image in grayscale mode
color = cv2.imread("galaxy.jpeg", 1)
# The images has 3 dimensions
print(color.ndim)

#Let's read the image in grayscale mode
gray = cv2.imread("galaxy.jpeg", 0)
#Print the dimensions of the image to check if it is in grayscale mode
print(gray.ndim)
# Let's convert the image to grayscale
gray_galaxy = cv2.imwrite("galaxy_gray.jpeg", gray)

for image in os.listdir('./images'):
    gray_image = cv2.imread(f'./images/{image}', 0)
    cv2.imwrite(f'./images/gray_{image}', gray_image)