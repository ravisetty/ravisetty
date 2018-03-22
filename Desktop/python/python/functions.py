# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 11:12:07 2016

@author: ymlui
"""

def foo1():
    print 'This is a function!'

def foo2(name, age=25):
    print('%s is %d years of age'%(name,age))
    
# * indicates variable length of argments    
def foo3(firstarg, *restarg):    
    print firstarg
    for i in restarg:
        print i
        
        
def foo4(num):
    a = num
    b = num**2
    c = pow(num, 3)
    
    return a,b,c
        
############### main function #################    
if __name__ == '__main__':  
    foo1()
    foo2('Peter')
    foo2('Peter',40)
    
#    list = [10, 20, 30, 40]
#    for i in list:
#        print i
#    foo3(10, 20, 30, 40)
#    
#    [a,b,c] = foo4(2)
#    print('%d %d %d'%(a,b,int(c)))