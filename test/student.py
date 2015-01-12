#!/usr/bin/env python
# coding=utf-8

class Student(object):
    def __init__(self, name, score):
        self.name=name
        self.score=score
    def print_score(self):
        print '%s: %s' %(self.name,self.score)

if __name__=='__main__':
    bart = Student('Bart Simpson',59)
    Lisa = Student('Lisa Simpson',87)
    bart.print_score()
    Lisa.print_score()
    print '--------------------'
    print bart.name
    bart.name ='111111111'
    print bart.name
    bart.a=1
    print bart.a
