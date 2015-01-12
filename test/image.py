#!/usr/bin/env python
# coding=utf-8

import Image
im = Image.open('test.png')
print im.format, im.size, im.mode
