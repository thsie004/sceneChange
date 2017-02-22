#! /usr/bin/env python

import os
import numpy as np
import matplotlib.pyplot as plt
import Image
import glob as g
import cv
from math import floor
import time
import csv

preName = 'BasketballCut'
frameStep = 2

# maxDim is the size of the reduced image that we use.
maxDim = 32

movieName = preName + '.mp4'
cdir = os.getcwd()
wdir = cdir
fileName = movieName

frameOutName = "frame"
os.chdir(wdir)


# initiate movie stream
capture = cv.CaptureFromFile(movieName)
#NframesTot = 400
NframesTot = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_COUNT))
frameRate = (cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FPS))

totalTime = NframesTot/frameRate
totalTime = round(totalTime)
print totalTime

intervals = int(totalTime/0.2)
print intervals

Nframes = floor(float(NframesTot)/float(frameStep) + 1.5)

framesArray = np.zeros( (int(Nframes), maxDim, maxDim), dtype=complex)
output_array = np.zeros( intervals)
times_array = np.zeros( intervals)
j = 0

for k in xrange(0, intervals):
	frame1 = cv.QueryFrame(capture)
	#if k % frameStep == 0:
	if maxDim:
        	size = cv.GetSize(frame1)
                maxFrameDim = max(size)
                scale = float(maxFrameDim)/float(maxDim)
                newSize = (int(floor(size[0]/scale + .5)), \
                                                int(floor(size[0]/scale + .5)) )
                smallFrame = cv.CreateImage(newSize, frame1.depth, frame1.nChannels)
                cv.Resize(frame1, smallFrame)
                Im1 = np.array(smallFrame[:]).mean(axis=2)
                #D = Im1.shape
                Im1 = np.fft.fft(Im1)
		framesArray[j::] = Im1
		j += 1
			
framesArray /= np.linalg.norm(framesArray)


for j in xrange(0, intervals):
	
	Im1 = framesArray[j]
	Im2 = framesArray[j+1]
	squared = np.square(np.abs(Im2-Im1))
	output_array[j] = np.sqrt(np.sum((squared)))
	t = (0.2*float(j))
	#t = round(t, 2)
	times_array[j] = t

with open('Basketball.csv', 'a') as csvFile:
	table = csv.writer(csvFile, delimiter=',')
	table.writerow(output_array)	
	table.writerow(times_array)
