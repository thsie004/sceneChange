# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 12:20:10 2014

@author: Tom
"""

import csv

x = [1,2,3,4]

with open('eggs.csv', 'a') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(x)