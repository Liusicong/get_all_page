#/usr/bin/python
# coding:utf-8
# File: get_first_url.py

import HTMLParser

class GetFirstUrl_HTMLParser(HTMLParser.HTMLParser):
    
    def __init__(self):
        self.processing=None
        self.href=[]
        self.jobname=[]
        HTMLParser.HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if (tag=='a'
            and "onclick" in attrs
            and attrs.get('onclick') == "javascript:dyweTrackEvent('souhomesearchtag','jobnavunfold');"):
            self.processing=tag
            self.href.append(attrs.get('href'))

    def handle_data(self, data):
        if self.processing:
            self.jobname.append(data)

    def handle_endtag(self, tag):
        if self.processing==tag:
            self.processing=None

import urllib
import get_page
import re

url = "http://sou.zhaopin.com/"

html = urllib.urlopen(url).read()

parser = GetFirstUrl_HTMLParser()

parser.feed(html)

# 注意'.'和'?'都是正则表达式的特殊符号
re_url = re.compile(r'^/jobs/searchresult\.ashx\?jl=763&bj=\d+$')

filename = '/home/liusic/thesis/data/first_url/'

for (u,j) in zip(parser.href, parser.jobname):
    if re_url.match(u):
        j = j.replace('/','|')
        get_page.get_page("http://sou.zhaopin.com"+u,filename+j+'.html')
        
