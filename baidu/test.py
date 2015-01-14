#!/usr/bin/env python
# -*- coding: utf-8 -*-

from baidupan.baidupan import BaiduPan

if __name__ == '__main__':
    access_token=''
    disk=BaiduPan(access_token)
    print disk.quota()
    print disk.upload('hello', path='/apps/appname/hello')
