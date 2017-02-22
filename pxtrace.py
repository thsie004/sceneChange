# TRACE COMPARISON

# LIBRARIES
import cv2
import numpy as np

# VARIABLES
resize_length = 300 # length of resized image



def trace_counts(frame1,frame2):
    
    # LOADING AN IMAGE
    img1 = cv2.imread('black1.jpg',1)
    img2 = cv2.imread('black2.jpg',1)

    # VARIABLES
    trace1 = np.zeros(3) # trace of img1R
    trace2 = np.zeros(3) # trace of img2R
    trace_counts = 0 # scene change counts
    trace_diff = np.zeros(3) # difference between pixels
    trace_thresh = 1 # difference threshold


    # RESIZING AN IMAGE
    img1R = cv2.resize(img1, (resize_length, resize_length))
    img2R = cv2.resize(img2, (resize_length, resize_length))

    # DISPLAYING RESIZED IMAGES
    """
    cv2.imshow('image1R',img1R)
    cv2.imshow('image2R',img2R)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    """

    # FIND TRACE OF 2 IMAGES
    for i in xrange(0,resize_length):

        for j in xrange(0,resize_length):
        
            if i == j: 
                trace1 = trace1 + img1R[i,j]
                trace2 = trace2 + img2R[i,j]

    # SUBTRACT TRACES
    trace_diff = abs(np.add(trace1,trace2))

    # INCREMENT 'counts' only if 'trace_diff' is below 'thresh'
    if trace_diff[0] >= trace_thresh and trace_diff[1] >= trace_thresh and trace_diff[2] >= trace_thresh:
        trace_counts += 1
        # TODO: record time of scene change

    # PRINT COUNTS VALUE 
    print 'trace_counts = ', trace_counts
    
    return trace_counts
                          
