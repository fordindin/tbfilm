#!/usr/bin/env python
import GetPage
import config
import HTMLParser as parser

def unseen(args):
    page = GetPage.getpage(config.series_page)["page"]
    data = parser.unseen(page)
    print ""
    for e in data:
        if e[1] >= 3: ch = '>='
        else: ch = '=='
        print "\t%s %s\t%s" % (ch, e[1], e[2])
    print "\n" + "-"*50
    print "\t" + parser.epcount(page)
