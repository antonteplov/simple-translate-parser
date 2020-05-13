# coding: utf-8
# Для проекта TTA
# Модуль  для подсчета уникальных одинарных  слов.
import re
import pymorphy2

Mor = pymorphy2.MorphAnalyzer()


def proceed(fraza, W, BL=[]):
    analyzed_words=0
    for word in fraza:
        if not re.search(r'[a-z]',word):
            #print("%s %d" % (word , len(word)))
            p = Mor.parse(word)[0]
            word = p.normal_form
            if word not in BL:
                analyzed_words +=1
                if word in W:
                    W[word] += 1
                else:
                    W[word]=1
    return analyzed_words
    