# -*- coding: utf-8 -*-
"""
Created on Mon May 15 14:49:24 2017

@author: ymlui
"""

import numpy as np

#X = np.zeros([5,5])
#print X

X = np.matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
#print X
#print X.shape
#



#print X.transpose()
#print X.shape
#
#print X
#print X[:,1:3]

Y = np.array([2,1,3,2,5,4,2,1,2,3])
#print len(Y)
#print Y.shape
#print np.matrix(Y).shape
#
#print np.where(Y == 1)
#print np.where(Y == 1)[0]

#print Y
#print np.unique(Y)
#
#print X
#print mean(X, axis=0) ## average for rows
#print mean(X, axis=1) ## average for columns

#u = mean(X, axis=1)
#print X - u


X1 = np.matrix([[1,2],[2,1]])
X2 = np.matrix([[2,1],[1,2]])
print np.dot(X1, X2)

