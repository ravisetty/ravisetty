# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 10:50:48 2016

@author: ymlui
"""

# adding from 1 to 10
sumval = 0
for i in range(11, 1,-2):
    sumval += i
    print i
    
print sumval  

# adding from 1 to 10 incremented by 2
#sumval = 0
#for i in range(1, 11, 2):
#    sumval += i
#    print i
#    
#print sumval    
#
## adding from 11 to 1 decremented by 2
#sumval = 0
#for i in range(11, 1, -2):
#    sumval += i
#    print i
#    
#print sumval    
#
## while loop
#i = 1
#sumval = 0
#while (i <= 10):
#    sumval += i
#    print i
#    i += 1
#    
#print sumval
#
#
## comparisons
#a = 'John'
#b = 'Peter'
#c = 'John'
#
list = [123, 456, 789, 1234, 456]
##print (a==b)
##print (a==c)
#
#if (list[0] == 999):
#    print '999'
#    print 'we are done'
#elif (list[1] >= 500 or list[2] < 800):
#    print 'Larger than 500 or less than 800'
#elif (list[2] != 789):
#    print 'Not 789'
#else:     
#    print "none of the above"

## sorting
#print 'Sorting ...' 
#print sorted(list)   
#print sorted(list, reverse=True)
#
#
## find
#print 'Find ...'
#print list.index(456)
#
## find all indices
index = [j for j,x in enumerate(list) if  x == 456]
print index