#!/usr/bin/env python

def person(name, age, **kwi):
    print 'name:', name, 'age:', age, 'other:', kwi
person('M', 30, city='Beijing', xx='asd')
