#!/usr/bin/env python

import urllib, getpass
from urllib import request
#from xml.etree.ElementTree import ElementTree
#import StringIO
#import xml.dom.minidom
#import os, re, time

from tbfilm.TurboAuth import TurboAuth
from tbfilm import config
import ssl


p = TurboAuth(config.login)

def auth(login):
    if not p.check_ssid():
        p.set_password(getpass.getpass("password for %s:" % config.login))
        p.get_cookies()

def getpage(url, data={}, headers={}):
    data = urllib.urlencode(data)
    auth(config.login)
    #req = urllib2.urlopen(url)
    req = request.Request(url, data, headers)
    response = request.urlopen(req)
    return {"page": response.read().decode('utf-8')}
