#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# 2014-10-29 5.2. myke: ping-pong for docker

from __future__ import division, print_function

#import sqlite3 as sql
import datetime as dt
#import os
#import string, re

from bottle import *

__author__  = 'myke'
__version__ = '5.2'
#DATABASE    = 'data/ap.db'

@get('/')
def index():
    dtoday = dt.datetime.now()
    dout = str(dtoday.isoformat())
    return "this is bottle at ", dout

@get('/ping')
def getter():
    dtoday = dt.datetime.now()
    dout = str(dtoday.isoformat())
    return "pong at ", dout

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)

