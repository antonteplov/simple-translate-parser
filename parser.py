#!/usr/bin/python3
# coding: utf-8
# Импортирует поддержку UTF-8.
from __future__ import unicode_literals
from html.parser import HTMLParser
import requests # для отправки HTTP GET/POST  запросов
import sys

class MyHTMLParserV(HTMLParser):
    flag=0
    R=list()
    def handle_starttag(self, tag, attrs):
        if tag=="f":
            self.flag=1;
        else:
            self.flag=0;

    def handle_endtag(self, tag):
        if tag=="f":
            self.flag=0;

    def handle_data(self, data):
        if self.flag==1 and not data in self.R:
            self.R.append(data)          

class MyHTMLParserN(HTMLParser):
    flag=0
    R=list()
    def handle_starttag(self, tag, attrs):
        if tag=="span" and len(attrs)>0 and ( "transl_form" in attrs[0] or "transl_form ins" in attrs[0]):
            self.flag=1            
        else:
            self.flag=0

    def handle_endtag(self, tag):
        if tag=="span":
            self.flag=0;

    def handle_data(self, data):
        if self.flag==1 and not data in self.R:
            self.R.append(data)          



if len(sys.argv) < 3:
    print ("Use %s <v|n> <word>" % (sys.argv[0]))
    print ("Example: %s v бухать" % (sys.argv[0]))
    print ("Example: %s n водка" % (sys.argv[0]))
    print ("Example: %s n синий" % (sys.argv[0]))
    exit()
if sys.argv[1] not in ('v','n'):
    print ("First argument error!")
    exit()

word = sys.argv[2]
r = requests.get("https://www.translate.ru/grammar/ru-en/"+word)
# print (r.text)

if sys.argv[1]=='v': parser = MyHTMLParserV()
if sys.argv[1]=='n': parser = MyHTMLParserN()
parser.feed(r.text)
for r in parser.R:
    print (r)
    

