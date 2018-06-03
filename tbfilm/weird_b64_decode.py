#!/usr/bin/env python

from base64 import b64decode

def w_base64_decode(s):
    a = "xuYokngrmTwfdcesilytpbzaJv"
    b = "2I0=3Q8V7XGMRUH41Z5DN6L9BW"

    for i,v in enumerate(a):
        s = s.replace(v, '___').replace(b[i], v).replace('___', b[i])

    return b64decode(s)
