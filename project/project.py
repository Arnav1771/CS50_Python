'''
Pixated Camera Demo
Name : Arnav Bhargava
Github : https://github.com/Arnav1771
edX Username : arnavbh_7
City : Delhi
Country : India
#Date : 08/17/2024
'''

import cv2
import numpy as np
from PIL import Image, ImageDraw


DOT_SIZE = 16
RADIUS = DOT_SIZE // 2

cv2.namedWindow("Pixated Camera")
vc = cv2.VideoCapture(0) # probably 0 if you have 1 webcam, see note below

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

def convert(source_img):
    width, height = len(source_img), len(source_img[0])
    dotted_img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(dotted_img)
    for x in range(0, width, DOT_SIZE):
        for y in range(0, height, DOT_SIZE):
            color = source_img[x][y]
            shape = [(x - RADIUS, y - RADIUS),
                     (x + RADIUS, y + RADIUS)]
            # we need to change the color space from BGR to RGB
            draw.ellipse(shape, # cv2 does weird stuff
                         fill=tuple([color[2], color[1], color[0]]))
    return cv2.cvtColor(np.asarray(dotted_img), cv2.COLOR_RGB2BGR)

while rval:
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    frameEdited = convert(frame)
    cv2.imshow("preview", frameEdited)

    if key == 27: # exit on ESC
        break

cv2.destroyWindow("preview")
