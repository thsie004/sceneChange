# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 20:50:48 2014

@author: Tom
"""

import SCMetric as scm

class SCFrame:
    """
        This class object stores the matrix itself and its information
        extracted from the metric functions.
        
        TODO: better doc string with function names listed
    """
    
    def __init__(self, matrix, fIndex = None, tPosition = None):
        """
            Class object constructor
            
            __init__(self, matrix)
            
            @param matrix A numpy array or OpenCV image matrix.
        """
        self.frame = matrix
        
        if fIndex is not None:
            self.index = fIndex
        else:
            self.index = 0
            
        if tPosition is not None:
            self.time = tPosition - 40
        else:
            self.time = 0.0
            
        #self.numLines = scm.houghLineCheck(self.frame)
        #self.hueList = scm.hueCheck(self.frame)