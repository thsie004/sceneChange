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

def main():
    """
        The main looping body for our metric functions. At any given iteration
        of the loop other than the first, there will be two matrices available
        as the input argument to our metric functions.
        
        No parameter is required, though we can definitely change that to where
        we take the video-finding part out of this block of code, and make this
        block of code take in a video stream as an input parameter.
    """
    
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
                    cv2.imshow(videoName, matrixA.frame)
                else:
                    matrixB = scf.SCFrame(frame, fIndex, stream.get(0))
                    cv2.imshow(videoName, matrixB.frame)
                
                if iterationNum > 0:

                    
                    pass
                
            else:
                errorCount += 1
                print "Frame %d could not be extracted." % fIndex
                
                if errorCount == 3:
                    print "Failed to extract too many frames, program quitting."
                    break;
            
            #Pressing q on your keyboard breaks the video being played.
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            fIndex += frameGap
            iterationNum += 1
            
    else:
        print "Video was not loaded into the stream."
        errorCount = 3

    if errorCount < 3:
        print "Looped successfully!"
    
    stream.release()
    cv2.destroyAllWindows()


if __name__ is '__main__':
    main()
    