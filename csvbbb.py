# -*- coding: utf-8 -*-
"""
Created on Mon Nov 03 18:27:18 2014

@author: Tom
"""

import cv2
import numpy as np
import os
from math import floor
import SCFrame as scf
import csv
import NaiveMetrics as nm

def minus(x, y):
    return abs(x-y)

def main():
    """
        The main looping body for our metric functions. At any given iteration
        of the loop other than the first, there will be two matrices available
        as the input argument to our metric functions.
        
        No parameter is required, though we can definitely change that to where
        we take the video-finding part out of this block of code, and make this
        block of code take in a video stream as an input parameter.
    """
  
    with open('SumBookofMormonDiff.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(["Interval(second)", "B","G","R"])

        #Requires this .py file to be in the same directory as the video file.
        #Video file needs to be .mp4 or change the last string section in stream init.
        videoPath = os.getcwd()
        videoName = raw_input("Enter video name: ")
        stream = cv2.VideoCapture(videoPath+'\\'+videoName+".mp4")
        
        fIndex = 0  #Frame index, used to jump around frames.
        totalFrames = int(stream.get(7))
        FPS = int(stream.get(5)) #Frames per second.
        dimension = (int(floor(stream.get(3)/2)), int(floor(stream.get(4)/2))) #For resizing to 1/4 of the original image.
        frameGap = input("Gap between frames? (FPS: %0d): " % FPS)  #E.g. frame #0 and frame # 10 has a gap of 10.
        
        matrixA = scf.SCFrame(np.zeros((dimension[0], dimension[1], 3), np.uint8))
        matrixB = scf.SCFrame(np.zeros((dimension[0], dimension[1], 3), np.uint8))
        
        iterationNum = 0    
        errorCount = 0        
        
        if stream.isOpened():
            while fIndex < totalFrames:
                stream.set(1, fIndex)
                
                #If a frame is captured, ret == true and frame == captured matrix.
                ret, frame = stream.read()
                
                #TODO: Potential bugs may exists if the program skips a frame when
                #      extracting matrices, making matrixA and matrixB
                #      non-continuous. Can implement something to prevent this.
                if ret:
                    frame = cv2.resize(frame, dimension)
                    
                    if iterationNum % 2: #Condition evaluates to either 1 or 0
                        matrixA = scf.SCFrame(frame, fIndex, stream.get(0))
                        #cv2.imshow(videoName, matrixA.getFrame())
                    else:
                        matrixB = scf.SCFrame(frame, fIndex, stream.get(0))
                        #cv2.imshow(videoName, matrixB.getFrame())
                    
                    if iterationNum > 0:
                        
                        if iterationNum%2:
                            #spamwriter.writerow(["%f to %f" % (round(matrixB.time/1000.0,2), round(matrixA.time/1000.0,2)), abs(matrixA.numLines-matrixB.numLines)])
                            #spamwriter.writerow(["%f to %f" % (round(matrixB.time/1000.0,2), round(matrixA.time/1000.0,2))]+map(minus, matrixA.hueList, matrixB.hueList))
                            spamwriter.writerow(["%f to %f" % (round(matrixB.time/1000.0,2), round(matrixA.time/1000.0,2))]+nm.RandomDiff(matrixA.frame, matrixB.frame))
                            
                        else:
                            
                            #spamwriter.writerow(["%f to %f" % (round(matrixA.time/1000.0,2), round(matrixB.time/1000.0,2)), abs(matrixA.numLines-matrixB.numLines)])
                            #spamwriter.writerow(["%f to %f" % (round(matrixA.time/1000.0,2), round(matrixB.time/1000.0,2))]+map(minus, matrixA.hueList, matrixB.hueList))
                            spamwriter.writerow(["%f to %f" % (round(matrixA.time/1000.0,2), round(matrixB.time/1000.0,2))]+nm.RandomDiff(matrixA.frame, matrixB.frame))
                        
                    
                else:
                    errorCount += 1
                    print "Frame %d could not be extracted." % fIndex
                    
                    if errorCount == 3:
                        print "Failed to extract too many frames, program quitting."
                        break;
                

                
                fIndex += frameGap
                iterationNum += 1
                
        else:
            print "Video was not loaded into the stream."
            errorCount = 3
    
        if errorCount < 3:
            print "Looped successfully!"
        
        stream.release()

if __name__ is '__main__':
    main()
    