#!/usr/local/bin/env python
print("hello world!")
def a(x):
    print 'a:%s'%x
def b(y):
    print 'b:%s'%y
def c(b):
    b('xx')
     
if __name__=='__main__':
    c(a)
