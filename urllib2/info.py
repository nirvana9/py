#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

old_url = 'http://nienie.im/'
req = Request(old_url)
response = urlopen(req)
print 'Info():'
print response.info()
