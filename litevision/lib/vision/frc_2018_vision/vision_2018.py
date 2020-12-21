import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

def show_cam():
    _, img_bgr = cap.read()
    img_rgb = cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)
    img_rgb = img_rgb.swapaxes(0, 1)
    return img_rgb


def process_18():    
    box = 0
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(2,2))
    _, img_bgr = cap.read()
    
    min_green = np.array([57, 100, 100])
    max_green = np.array([97, 255, 255])
    
    img = cv.cvtColor(img_bgr, cv.COLOR_BGR2HSV)

    mask = cv.inRange(img, min_green, max_green)
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        #for not rotated rectangle
        #x,y,w,h = cv.boundingRect(contour)
        #cv.rectangle(img_bgr,(x,y),(x+w,y+h),(0,255,0),2)
        rect = cv.minAreaRect(contour)
        box = cv.boxPoints(rect)
        box = np.int0(box)
        cv.drawContours(img_bgr,[box],0,(0,255,0),2)
        left = box[2][1]
        right = box[0][1]
        top = box[1][0]
        bot = box[3][0]
        midy = int((bot + top)/2)
        midx = int((right + left)/2)
        cv.circle(img_bgr, (midy, midx), 5, (255, 0, 0), 5)        
        
    img_rgb = cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB) 
    img_rgb = img_rgb.swapaxes(0, 1)
     
    return img_rgb, box
        