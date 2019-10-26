#!/usr/bin/python3
# coding: utf-8
# Импортирует поддержку UTF-8.
from __future__ import unicode_literals
from html.parser import HTMLParser
import requests # для отправки HTTP GET/POST  запросов
import sys
import time
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




def Parse(word):    
    r = requests.get("https://www.translate.ru/grammar/ru-en/"+word)
    #print (r.text)
    Txt = r.text
 
    parser = MyHTMLParserV()    ## Глаголы 
    parser.R=[word]
    parser.feed(Txt)
    if len(parser.R)!=0:
        for r in parser.R:
          print (r)
    parser.close()
    parser.reset()
    parser.R=list()
    parser = MyHTMLParserN()  ## Существительные и прилагательные
    parser.R=list()
    parser.feed(Txt)
    if len(parser.R)!=0:
        for r in parser.R:
          print (r)
    parser.close()
    parser.reset()
    parser.R=list()
    time.sleep(2)  ## Чтобы не замучать сайт
    return

def main():
    if len(sys.argv) < 2:
        print ("TeplovParser v%s" % 1)
        print ("Use %s  <word1> [word2] .. [wordN]" % (sys.argv[0]))
        print ("Example: %s  бухать" % (sys.argv[0]))
        print ("Example: %s  водка пиво" % (sys.argv[0]))
        print ("Example: %s  синий нос торчит" % (sys.argv[0]))
        exit()
    i=1;
    while i < len(sys.argv):
        Parse(sys.argv[i])
        i+=1
 
if __name__ == "__main__":  main()
