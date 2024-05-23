import cv2
import numpy as np
def crad(name,second,id,years):
    image = cv2.imread('source/cardetud.png')
    # Specify the position (x, y) and text size
    text_size = 1
    # Define the font and color
    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (0, 0, 0)  # White color in BGR
    # Add text to the image
    cv2.putText(image, str(name), (220, 230), font, text_size, color, 2, cv2.LINE_AA)
    cv2.putText(image, str(second), (370, 291), font, text_size, color, 2, cv2.LINE_AA)
    cv2.putText(image, str(years), (336, 360), font, text_size, color, 2, cv2.LINE_AA)
    cv2.putText(image, str(id), (76, 562), font, text_size, color, 2, cv2.LINE_AA)
    cv2.imwrite(f'cards/{id}.jpg', image)
def brow(ID,ISBN,startdate,enddate,number) :
    image = cv2.imread('source/bo2.png')
    # Specify the position (x, y) and text size
    text_size = 1
    # Define the font and color
    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (0, 0, 0)  # White color in BGR
    # Add text to the image
    cv2.putText(image, str(ID), (340, 230), font, text_size, color, 2, cv2.LINE_AA)
    cv2.putText(image, str(ISBN), (370, 291), font, text_size, color, 2, cv2.LINE_AA)
    cv2.putText(image, str(startdate), (336, 360), font, text_size, color, 2, cv2.LINE_AA)
    cv2.putText(image, str(enddate), (360, 422), font, text_size, color, 2, cv2.LINE_AA)
    cv2.putText(image, str(number), (190, 562), font, text_size, color, 2, cv2.LINE_AA)
    cv2.imwrite(f'cards/{number}.jpg', image)
