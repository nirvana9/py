#!/usr/bin/env python

L = range(1,101)
L = range(1,101)
def is_s(n):
    if n ==1:
        return False
    if n==2:
        return True
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
print filter(is_s,L)
