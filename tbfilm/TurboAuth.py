#!/usr/bin/env python
# coding: utf-8

import urllib
import http.cookiejar as cookielib
import os, re, time
import ssl
import sys

import socket
import urllib.request as urllib2

from tbfilm import config
""" This module emulates Turbofilm.tv auth.
It checks cookies in given cookie jar, and put there
valid cookies in case of expiration"""


if config.myresolver:
    import config.myresolver
    dns.resolver.override_system_resolver(dns.resolver.Resolver(filename=config.myresolver) )

#dns.resolver.override_system_resolver( dns.resolver.Resolver(filename='resolv.conf') )
cj = config.cookie_path

class TurboAuth:
    def __init__(self, login, password=None):
        openers_list = []
        self.cookie_jar = cookielib.LWPCookieJar(filename=cj)
        if os.path.isfile(cj): self.cookie_jar.load(cj)
        # clear expired and session cookies

        self.cookie_jar.clear_expired_cookies()
        self.cookie_jar.clear_session_cookies()

        cookie_opener = urllib2.HTTPCookieProcessor(self.cookie_jar)
        openers_list.append(cookie_opener)
        # install cookies

        if config.ignore_ssl_certs:
            context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
            context.options |= ssl.OP_NO_SSLv2
            context.options |= ssl.OP_NO_SSLv3
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            https_opener = urllib2.HTTPSHandler(context=context)
            openers_list.append(https_opener)

            opener=urllib2.build_opener(*openers_list)
            urllib2.install_opener(opener)
            self.login = login
            self.set_password(password)

    def check_ssid(self):
        for e in self.cookie_jar:
            if e.name == "IAS_ID":
                return e.value
        return False

    def set_password(self, password):
        self.password = password

        def get_cookies(self):
            req = urllib2.urlopen(config.auth_url)

            datadict = {
                "login": self.login,
                "passwd": self.password,
                "remember": "on",
            }

            data = urllib.urlencode(datadict)
            req = urllib2.Request(config.auth_url, data, config.headers)
            response = urllib2.urlopen(req)
            the_page = response.read()
            self.cookie_jar.save(cj)
            return True

    @classmethod
    def clear_cookies(obj):
        os.remove(cj)
        return True
