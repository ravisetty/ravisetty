# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 11:31:11 2016

@author: ymlui
"""

# import other modules
import numpy as np
from pylab import *

class Data:
    def __init__(self, n, m):
        ## private attribute
        self.__data = np.zeros((n,m))
        
        ## public attributes
        self.rows = n
        self.cols = m
        
        self.printData()
        
    
    def printData(self):
        if (len(self.__data.shape) == 2):
            print self.__data
            print self.__data.shape
        
    def getData(self):
        return self.__data
        
    def diagAssign(self, val):
        if (self.__data.shape[0] == self.__data.shape[1]):
            self.__data[np.diag_indices_from(self.__data)] = val
            
            print 'Diag Assig ...'
            self.printData()
        else:
            print 'It is not a square matrix ...'
        
    def allAssign(self, val):
        self.__data[:] = val  
        
        print 'All Assign ...'
        self.printData()
        
    def __doSth(self):
        print 'doing something ...'
        
    def vectorize(self):
        return self.__data.flatten()        
        
############### main function #################    
if __name__ == '__main__':  
    
    d1 = Data(4,3)
    print('%d %d'%(d1.rows, d1.cols)) 
#    print d1.__data
#    d1.__doSth()
        
    d1.allAssign(2)
#    d1.diagAssign(3)
#    
#    x = d1.vectorize()
#    print x  
#    
#    y = x.reshape((4,3))
#    print y
    
    