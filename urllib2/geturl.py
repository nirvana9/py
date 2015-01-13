#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

old_url = 'http://nienie.im/lastestcomics.html'

req = Request(old_url)

response = urlopen(req)

print 'Old url :'+old_url
print 'Real url:'+response.geturl()
