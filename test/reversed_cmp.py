#!/usr/bin/env python

def reversed_cmp(x, y):
    if x>y:
        return -1
    if y>x:
        return 1
    return 0

print sorted([36,5,12,9,21], reversed_cmp)