#!/usr/bin/env python
# coding=utf-8


class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value, int):
            raise ValueError('socre must be an integer!')
        if value < 0 or value >100:
            raise ValueError('score must between 0 ~ 100!')
        self._score=value

s=Student()
s.score=90
print s.score
