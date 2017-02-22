# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 17:56:54 2014

@author: Tom
"""

import csv
from math import sqrt

def stdDevCheck(dictionary, thresholdMultiplier):
    
    data = dict.copy(dictionary)
    
    avg = 0.0
    
    for val in data.values():
        avg += val
    
    avg = avg / float(len(data.values()))
    
    devNumerator = 0.0
    
    for key in data:
        data[key] = (data[key] - avg) * (data[key] - avg)
        devNumerator += data[key]
    
    deviation = sqrt(devNumerator / float(len(data.values())))
    
    for key in dictionary:
        if abs(dictionary[key] - avg) > (deviation*thresholdMultiplier):
            dictionary[key] = 1
        else:
            dictionary[key] = 0
            
    print
    print "Scene changed detected in the following times:" 
    
    for key in sorted(dictionary):
        if dictionary[key] == 1:
            print key
    
    
def main():
    
    hueDict = {}    
    
    name = raw_input("CSV file name (exclude .csv handle): ")    
    
    name += ".csv"    
    
    thresholdMultiplier = 2.2
    
    with open(name, 'rb') as f:
        reader = csv.reader(f)
        reader.next()
        
        for row in reader:
            total = 0.0
            
            for x in range(1,len(row)):
                total += float(row[x])
            
            hueDict.update({row[0]: total})
    
    stdDevCheck(hueDict, thresholdMultiplier)
    
if __name__ == "__main__":
    main()
        
        
        