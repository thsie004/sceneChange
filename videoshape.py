# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 08:48:59 2014

@author: Tom
"""

import cv2

stream = cv2.VideoCapture("allstar.mp4")
if stream.isOpened():
    print stream.get(7)