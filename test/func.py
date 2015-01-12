#!/usr/bin/env python

def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args=', args, 'kw =', kw

func(1, 2, x='234')
