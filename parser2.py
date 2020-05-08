#!/usr/bin/python3
# coding: utf-8

# INSTALL
# pip install pymorphy2
# pip install pymorphy2-dicts
# pip install DAWG


# Импортирует поддержку UTF-8.
from __future__ import unicode_literals

import sys
import pymorphy2


def Parse(w):    
     morph = pymorphy2.MorphAnalyzer()
     p = morph.parse(w)[0]
     print(';'.join(('token','value','pos','tense')))
     for lex in p.lexeme:
            #print(lex)
            word = lex.word
            normal_form = lex.normal_form
            pos = lex.tag.POS
            if pos=="INFN": pos="verb"
            if lex.tag.tense:
                if lex.tag.tense=="pres": tense='present'
                if lex.tag.tense=="futr": tense='future'
            else:
                if pos=="VERB": 
                    tense='future'
                else:
                    tense = "na"

            out = ';'.join((word,normal_form,pos,tense))
            print(out.lower())
         
     return

def main():
    if len(sys.argv) < 2:
        print ("TeplovParser v%s" % 2)
        print ("Use %s  <word1> [word2] .. [wordN]" % (sys.argv[0]))
        print ("Example: %s  бухать" % (sys.argv[0]))
        print ("Example: %s  водка пиво" % (sys.argv[0]))
        print ("Example: %s  синий нос торчит" % (sys.argv[0]))
        exit()
    i=1
    while i < len(sys.argv):
        Parse(sys.argv[i])
        i+=1
 
if __name__ == "__main__":  main()
