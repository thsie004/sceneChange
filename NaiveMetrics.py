# NAIVE METRICS (trace, sum, random)


# LIBRARIES
import cv2
import csv
import numpy as np

# TRACE COMPARISON
def TraceDiff(frame1,frame2):
    
    # VARIABLES
    row = np.int32(frame1.shape[0]) # length of resized frame
    col = np.int32(frame1.shape[1]) # height of resized frame
    trace1 = np.zeros(3) # trace of frame1
    trace2 = np.zeros(3) # trace of frame2
    trace_diff = np.zeros(3) # difference between pixels
    
    # FIND TRACE OF BOTH FRAMES (frame1, frame2)
    for x in xrange(0,row):
        for y in xrange(0,col):
            if x == y: 
                trace1 = trace1 + np.int32(frame1[x,y])
                trace2 = trace2 + np.int32(frame2[x,y])

    # SUBTRACT TRACES
    trace_diff = abs(np.subtract(trace1,trace2))
    #print trace_diff


    
    z = trace_diff
    x = [z[0],z[1],z[2]]
    return x

# SUM OF PIXEL VALUES COMPARISONS
def SumDiff(frame1,frame2):

    # VARIABLES
    row = np.int32(frame1.shape[0]) # length of resized frame
    col = np.int32(frame1.shape[1]) # height of resized frame
    sum1 = np.zeros(3) # sum of pixel values in frame1
    sum2 = np.zeros(3) # sum of pixel values in frame2
    sum_diff = np.zeros(3) # difference in pixel values of frame1 & frame2

    # SUMMING PIXEL VALUES (for each frame)
    for x in xrange(0,row):
        for y in xrange(0,col):
            sum1 = sum1 + np.int32(frame1[x,y])
            sum2 = sum2 + np.int32(frame2[x,y])

    # SUBTRACT SUMS
    sum_diff = abs(np.subtract(sum1,sum2))

    z = sum_diff
    x = [z[0],z[1],z[2]]
    return x

# RANDOM PIXEL COMPARISONS
def RandomDiff(frame1,frame2):

    # VARIABLES
    row = np.int32(frame1.shape[0]) # length of resized frame
    col = np.int32(frame1.shape[1]) # height of resized frame
    iterations = int(0.10 * row) # amount of pixel comparison iterations
    random_diff = np.zeros(3) # difference between 2 pixels from frames

    # COMPARE RANDOM PIXELS
    for i in xrange(0,iterations):
    
        # Random pixel position
        x = np.random.randint(5,row-5)
        y = np.random.randint(5,col-5)
        
        # Random pixels' values
        random_px1 = np.int32(frame1[x,y])
        random_px2 = np.int32(frame2[x,y])
        
        # SUBTRACT PIXEL VALUES
        random_diff = abs(np.subtract(random_px1,random_px2))
    
    # APPEND 'random_diff' array to .csv file

    z= random_diff
    x = [z[0],z[1],z[2]]
    return x

"""

#Testing call of the functions
img1I = cv2.imread("black1.jpg", 1)
img2I = cv2.imread("black2.jpg", 1)

img1 = cv2.resize(img1I, (150, 150))
img2 = cv2.resize(img2I, (150, 150))

for loop in xrange(0,3):
    print 'TraceDiff=', TraceDiff(img1,img2)
    print 'SumDiff=', SumDiff(img1, img2)
    print 'RandomDiff=', RandomDiff(img1,img2) 
"""

cv2.waitKey(0)
cv2.destroyAllWindows()