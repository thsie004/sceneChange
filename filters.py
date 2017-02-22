# -*- coding: utf-8 -*-
"""
Created on Sun Nov 02 21:03:14 2014

@author: Tom
"""

import cv2
import os
import numpy as np

path = os.getcwd()+"\stuck"
os.chdir(path)

print path

test = cv2.imread('stuckFrame200.png')
test = cv2.resize(test, (640,360))


gray = cv2.cvtColor(test,cv2.COLOR_BGR2GRAY)

#3 different derivative methods
sobelTest = cv2.Sobel(gray, cv2.CV_8U, 1, 1, ksize=7)
cannyTest = cv2.Canny(gray,100,200, apertureSize = 3)
laplaceTest = cv2.Laplacian(gray, cv2.CV_8U)
matrix = np.zeros((cannyTest.shape[0], cannyTest.shape[1], 3), np.uint8)
#put into probabilistic hough and draws the lines
#you can choose which derivative to plug in by changing
#                       *********
lines = cv2.HoughLinesP(cannyTest,1,np.pi/90,30,100,10)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(test,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imshow("d",test)
#shows the lines drawn
#cv2.imshow("d",test)


#under this are the derivatives, uncomment to see them as a picture

#cv2.imshow("canny", cannyTest)
#cv2.imshow("sobel", sobelTest)
#cv2.imshow("laplace", laplaceTest)
cv2.imwrite("imagg.png", test)
cv2.waitKey(0)
cv2.destroyAllWindows()