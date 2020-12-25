import cv2 as cv
import numpy as np
import json

cap = cv.VideoCapture(0)

def get_color():
    with open(r"litevision\res\litevision.json") as f:
        color = json.load(f)

        h_min, h_max = 0, 0
        s_min, s_max = 0, 0
        v_min, v_max = 0, 0 
        
        h_max = max(float(color["min_color"]["hsva"]["h"]) / 2.01, float(color["max_color"]["hsva"]["h"]) / 2.01)
        s_max = max(float(color["min_color"]["hsva"]["s"]) * 2.55, float(color["max_color"]["hsva"]["s"]) * 2.55)
        v_max = max(float(color["min_color"]["hsva"]["v"]) * 2.55, float(color["max_color"]["hsva"]["v"]) * 2.55)
    
        h_min = min(float(color["min_color"]["hsva"]["h"]) / 2.01, float(color["max_color"]["hsva"]["h"]) / 2.01)
        s_min = min(float(color["min_color"]["hsva"]["s"]) * 2.55, float(color["max_color"]["hsva"]["s"]) * 2.55) 
        v_min = min(float(color["min_color"]["hsva"]["v"]) * 2.55, float(color["max_color"]["hsva"]["v"]) * 2.55)

        return (h_min, h_max), (s_min, s_max), (v_min, v_max)


def show_cam():
    _, img_bgr = cap.read()
    img_rgb = cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)
    img_rgb = img_rgb.swapaxes(0, 1)
    return img_rgb


def process_18():
    diff = 0
    box = 0

    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3))
    _, img_bgr = cap.read()
    width = img_bgr.shape[1]
    h, s, v = get_color()
    min_hsv = np.array([h[0], s[0], v[0]])
    max_hsv = np.array([h[1], s[1], v[1]])
    
    
    img = cv.cvtColor(img_bgr, cv.COLOR_BGR2HSV)

    mask = cv.inRange(img, min_hsv, max_hsv)
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
        midy = float((bot + top)/2)
        midx = float((right + left)/2)
        cv.circle(img_bgr, (int(midy), int(midx)), 5, (255, 0, 0), 5)        
        diff = abs(midx - width/2)
        
    img_rgb = cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB) 
    img_rgb = img_rgb.swapaxes(0, 1)
     
    return img_rgb, box