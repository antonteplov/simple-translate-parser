# coding: utf-8
# Для проекта TTA
# Модуль  для подсчета уникальных словосочетаний по ТРИ слова.
import re
import pymorphy2


Mor = pymorphy2.MorphAnalyzer()


def proceed(fraza, W, BL=[]):
    analyzed_words=0
    #### Лематизируем все слова в фразе
    l_fraza = []
    for  f in fraza: 
        p = Mor.parse(f)[0]
        if p.normal_form not in BL: 
            l_fraza.append(p.normal_form)
    fraza = l_fraza
    ###########################
    if len(fraza) >= 3:
        i = 0
        while i < len(fraza) - 2 :
            wordSet = " ".join((fraza[i],fraza[i+1],fraza[i+2]))
            #print("WS:{%s}" % wordSet)
            analyzed_words +=1
            if wordSet in W:
                W[wordSet] += 1
            else:
                W[wordSet]=1
            i = i + 3
            wordSet=""
            while i < len(fraza):
                #print ("ADD:{%s}" % fraza[i])
                analyzed_words +=1
                wordSet += fraza[i] + ' '
                i = i + 1
                if wordSet != "":
                    if wordSet in W:
                        W[wordSet] += 1
                    else:
                        W[wordSet]=1
    
    elif len(fraza)>0:
        wordSet = ' '.join(fraza)
        #print("SM:{%s}" % wordSet)
        analyzed_words +=1
        if wordSet in W:
            W[wordSet] += 1
        else:
            W[wordSet]=1
    return analyzed_words
