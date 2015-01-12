#!/usr/bin/env python

def fn(x,y):
    return x * y

print reduce(fn,[1,2,3,4,5])
