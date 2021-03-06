#!/usr/bin/env python
# coding: utf-8

import re
import os
import urllib
proto = "https:"

debug=False

turbofilm_base = 'https://turbik.tv'

proto_RE = re.compile("(http:|ftp:|https).*")

srt_urlRE=re.compile('https://(?:.*)/([0-9a-f]{32}).*')


sub_lang="en"
#sub_lang="ru"
sub_base="http://sub.turbik.tv/" +  sub_lang

login = "dindin@dindin.ru"

auth_url="https://turbik.tv/Signin"

#headers =  { 'User-Agent' : "Mozilla/5.0 compatible pure-python Turbofilm.tv client" }
headers =  { 'User-Agent' : "Mozilla/5.0 compatible" }

cookie_path = os.path.expanduser("~/.turbik.tv.cookie")

cdn_base_uri = "https://cdn.turbik.tv/"
cdn_authkey = "A2DC51DE0F8BC1E9"

quality="default"

max_fetch_retry = 12

wait_time = 1

series_page = "https://turbik.tv/My/Series"

watchUrl = 'https://turbik.tv/services/epwatch'

sdata_RE = re.compile("http(?:s)+://turbik.tv/Watch/(.*)/Season(.*)/Episode(.*)")
sdata_TMPL = "%s//turbik.tv/Watch/%s/Season%s/Episode%s"

wrkdir = "%s/turbofilm" % os.getenv("HOME")

offline_store = os.path.join(wrkdir, "offline.pickle")

socks_enable = False
#socks_enable = True
#socks_ip = "127.0.0.1"
#socks_port = 3555
socks_ip = "127.0.0.1"
socks_port = 9050
#myresolver="resolv.conf"
myresolver=False

ignore_ssl=False
ignore_ssl_certs=True

