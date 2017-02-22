#!/usr/bin/env python

import os
import numpy as np
import matplotlib.pyplot as plt
import Image
import glob as g
import cv2.cv as cv
import cv2
from math import floor
import time


preName = 'allstar'
frameStep = 2

# maxDim is the size of the reduced image that we use.
maxDim = 32

#function that returns fft matrix
#def fft_function(matrix)
	#return np.fft.fftn(matrix)
#----------------------------------------------------------
movieName = preName + '.mp4'
cdir = os.getcwd()
wdir = cdir
fileName = movieName

frameOutName = "frame"
os.chdir(wdir)


# initiate movie stream
capture = cv2.VideoCapture(movieName)
#NframesTot = 400
NframesTot = int(capture.get(7))

Nframes = floor(float(NframesTot)/float(frameStep) + 1.5)

framesArray = np.zeros( (int(Nframes), maxDim), dtype=complex)
j = 0
sumSceneChange = 0
output_array = np.zeros(int(Nframes))
#Im1 = np.zeros
#Im2 = np.zeros
#fft_info_array = np.zeros
for k in xrange(NframesTot):
	ret, frame1 = capture.read()
	if k % frameStep is 0  and k < NframesTot:
		if maxDim:
			size = frame1.shape
			maxFrameDim = max(size)
			scale = float(maxFrameDim)/float(maxDim)
			newSize = (int(floor(size[0]/scale + .5)), \
						int(floor(size[0]/scale + .5)) )
			frame1 = cv2.resize(frame1, newSize)
   
			Im1 = np.array(smallFrame[:]).mean(axis=2)
			#D = Im1.shape
			Im1 = np.fft.fft(Im1)
   
		if j is 0 or sceneChange is 1:
			ImRef = Im1
			ImNew = ImRef
   
		else:
			ImNew = Im1
			
	#Metric
		if k % frameStep < Nframes:
	    	    squared = np.square(np.abs(ImRef - ImNew))
	    	    output_array[j] = np.sqrt( np.sum((squared)))
          
		if output_array[j] > 18000.0:
		    sceneChange = 1
		    sumSceneChange+=1
      
		else:
		    sceneChange = 0
		j+=1
	
  	    
	


for item in output_array:
	print item
print sumSceneChange
