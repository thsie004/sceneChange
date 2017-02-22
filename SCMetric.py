# -*- coding: utf-8 -*-
"""
Created on Tue Nov 04 07:51:10 2014

@author: Tom
"""

import cv2
import numpy as np

def hueCheck(frame):
    """
        Takes in an image matrix and slice it up into 9 regions/sections after
        converting it into HSV color space for a more intuitive comparison
        method.
            -------------
            | 1 | 2 | 3 |  Each section is then blended into one single pixel
            -------------  value, and the hue (in HSV) element is stored in a
            | 4 | 5 | 6 |  python list. After all nine sections have their data
            -------------  extracted out, return the list.
            | 7 | 8 | 9 |
            -------------
        
        @param frame A numpy array or OpenCV image.
        @return A list containing nine elements, each being a hue value.
    """
    
    secInfo = []
    
    hframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    yBase = hframe.shape[0]
    xBase = hframe.shape[1]
    
    sec1 = frame[0:yBase/3,0:xBase/3]
    sec2 = frame[0:yBase/3,xBase/3:xBase*2/3]
    sec3 = frame[0:yBase/3,xBase*2/3:xBase]
    
    sec4 = frame[yBase/3:yBase*2/3,0:xBase/3]
    sec5 = frame[yBase/3:yBase*2/3,xBase/3:xBase*2/3]
    sec6 = frame[yBase/3:yBase*2/3,xBase*2/3:xBase]
    
    sec7 = frame[yBase*2/3:yBase,0:xBase/3]
    sec8 = frame[yBase*2/3:yBase,xBase/3:xBase*2/3]
    sec9 = frame[yBase*2/3:yBase,xBase*2/3:xBase]
    
    for i in range(0,9):
        exec("temp = cv2.mean(sec%d)" % (i+1))
        secInfo.append(round(temp[0], 2))
    
    return secInfo
    
    
def houghLineCheck(frame):
    """
        Takes in a image matrix, performs Canny derivative function, and then
        apply the Hough probabilistic onto the derivative. Returns the number
        of lines found using this method.
        
        @param frame A numpy array or OpenCV image.
        @return The number of lines found using HoughP on Canny derivative.
    """
    
    derivative = cv2.Canny(frame,100,200, apertureSize = 5)
    
    lines = cv2.HoughLinesP(derivative,1,np.pi/90,30,100,10)
    
    try:
        numLines = len(lines[0])
    except:
        #If no lines were found, the length of lines[] will be a NoneType,
        #causing an error.
        numLines = 0
        
    return numLines

