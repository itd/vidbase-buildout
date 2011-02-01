#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8
"""
fetch_live_loop.py
Grabs the live xml feed every 10 seconds


./fetch_live_loop.py > /web/log/fetchlivexmls-errors.txt &

"""

#import os
#import re
#import shutil
import time
import datetime
import urllib

kytargetdir = '/home/msworks/www/kyxml/'
kydtargetdir = '/home/msworks/gooch/'
kyurlprefix = 'http://vid.mandsworks.com/ky/'

#    ('xmlsource','targetpath','outfile'),
xmls = [
    (kyurlprefix+'kyannounce/iphoneannounce.xml',kytargetdir,'live.xml'),
    ]

def getNow():
  """Just return the current time for timestamping logs"""
  return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def fetchxmldata(xmlsrc):
    """"""
    sock = urllib.urlopen(xmlsrc)
    data = sock.read()
    sock.close()
    return data


def createfiles(xmls):
    """"""
    for item in xmls:
        xmlsrc =     item[0]
        targetpath = item[1]
        outfile =    item[2]
        data = fetchxmldata(xmlsrc)
        if data.startswith('<rss'):
            f = open(targetpath+outfile,'w')
            f.write(data)
            f.close()
            print "%s; got %s" % (getNow(), outfile)


def main():
    while 1 == 1:
        createfiles(xmls)
        time.sleep(10)


if __name__ == '__main__':
    main()