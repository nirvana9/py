#!/usr/bin/env python

def low(x):
    ch=''
    for k,v in enumerate(x):
        if k==0:
            ch+=v.upper()
        else:
            ch+=v.lower()
    return ch
old=['adam','LISA','barT']
print map(low,old)
