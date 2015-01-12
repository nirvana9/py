#!/usr/bin/env python
# coding=utf-8

class Student(object):
    def __init__(self, name):
        self.name=name
    def __str__(self):
        return "---------------------"
print Student('Michael')
