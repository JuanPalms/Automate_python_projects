"""
This python module contains more functions that are used to process the images
"""
import cv2
import os

def calculate_size(scale_percentage, width, height):
    """
    This function calculates the size of the image
    """
    new_width = int(width * scale_percentage / 100)
    new_height = int(height * scale_percentage / 100)
    return (new_width, new_height)

def resize_image(image_path, scale_percentage, resized_image_path):
    """
    This function resizes the image
    """
    image=cv2.imread(f"{image_path}", 1)
    new_dim = calculate_size(scale_percentage, image.shape[1], image.shape[0])
    resized_image = cv2.resize(image, new_dim)
    cv2.imwrite(resized_image_path, resized_image)


# Resize multiple images
for image in os.listdir("./images"):
    image_path = os.path.join("./images", image)
    resized_image_path = os.path.join("./resized_images", image)
    resize_image(image_path, 10, resized_image_path)