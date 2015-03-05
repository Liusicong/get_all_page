#!/usr/bin/env python
# -*- coding:utf-8 -*-
# File: get_page.py

import urllib

def get_page(url,filename):
    text = get_text(url)
    write_file(filename, text)
        
def get_text(url):
    result = urllib.urlopen(url)
    text = result.read()
    return text

def write_file( filename, content):
    with open(filename,'w') as fw:
        fw.write(str(content))
