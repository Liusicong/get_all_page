#/usr/bin/python
# coding:utf-8
# File: get_second_url.py

import HTMLParser
import re

import sys 
reload(sys) 
sys.setdefaultencoding('utf8')

re_url = re.compile(
    r"^/jobs/searchresult\.ashx\?jl=763&ispts=1&isfilter=1&p=1&bj=\d+&sj=\d+$"
)



class GetSecondUrl_HTMLParser(HTMLParser.HTMLParser):
    
    def __init__(self):
        self.processing=None
        self.href=[]
        self.jobname=[]
        self.tmp=''
        HTMLParser.HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if (tag=='a'
            and "href" in attrs
            and re_url.match(attrs.get('href'))):
            self.processing=tag
            self.href.append(attrs.get('href'))

    def handle_data(self, data):
        if self.processing:
            self.tmp = self.tmp + data

    def handle_endtag(self, tag):
        if self.processing==tag:
            self.processing=None
            self.jobname.append(self.tmp)
            self.tmp=''

import urllib


def get_second_url(url):

    html = urllib.urlopen(url).read()

    parser = GetSecondUrl_HTMLParser()
    parser.feed(html)

    result = [(j.replace('/','|'),u) for (j,u) in zip(parser.jobname, parser.href)]
    return result

if __name__=='__main__':
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=763&bj=4010200'
    result = get_second_url(url)
    for (j,u) in result:
        print('%s:\n%s' % (j,u))
