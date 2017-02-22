# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 22:43:51 2014

@author: Tom
"""
import multiprocessing
import py2exe
def worker(num):
    """thread worker function"""
    print 'Worker:', num
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()