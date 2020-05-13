#!/usr/bin/python3
# coding: utf-8

# INSTALL
# pip install pymorphy2
# pip install pymorphy2-dicts
# pip install DAWG


# Импортирует поддержку UTF-8.
from __future__ import unicode_literals
import re
import sys
import time
import pymorphy2

import tta_module_1w
import tta_module_2w
import tta_module_3w
import tta_module_4w





INFO = {
    'filename': "",
    'total_lines': 0,
    'total_raw_words': 0,
    'analyzed_words':0

    }

BL = []

Mor = pymorphy2.MorphAnalyzer()

def getLemma(w):    
     morph = pymorphy2.MorphAnalyzer()
     p = morph.parse(w)[0]
     return p.normal_form    

def getWords(line):
    line = re.sub(r"[#%!@*,.;:?(){}_/\"]", "", line)  #удаляем ненужные символы
    line = re.sub(r"\s+"," ",line)  # удаляем лишние пробелы
    line = line.strip() #удаляем символы пробелов в начале и конце строки
    line = line.lower()
    return line.split(' ') 


def main():
    W ={}  
    if len(sys.argv) < 4:
        print ("Teplov Text Analyzer (TTA) v%s" % 1)
        print ("Use %s <1|2|3|4> <input file> <output file> [blacklist file]" % (sys.argv[0]))
        print ("Первый параметр - число, указывающее на кол-во слов в словосочетаниях для анализа\nInput file содержит текстовые строки - одна строка , одна фраза для анализа\n Output file  будет содержать отчет о выполненной работе в формате CSV. Слова или словосочетания будут приведены в нормальную форму и проведен подсчёт вхождений такий простых конструкций.\n В качестве необезательного параметра можно указать имя файла blacklist. В этом файле одна строка=одно слово, которое будет исключаться из анализа.")
        exit()
    print ("Try open input file %s" % (sys.argv[2]) )
    try:
        Fin = open(sys.argv[2])
    except:
        print("Exception: Can't open file")
    else:
        print("Try open output file %s" % (sys.argv[3]) )
        try:
            Fout = open(sys.argv[3],'w')
        except:
            print("Exception: Can't open file") 
        else:
            INFO['filename'] = sys.argv[2]
            for line in Fin:
                INFO['total_lines'] +=1
                INFO['total_raw_words'] += len (getWords(line))
                #print(line)
                
            
            if len(sys.argv) == 5:
                print("Try open black list file %s" % (sys.argv[4]) )
                try:
                    Fbl = open(sys.argv[4])
                except:
                    print("Exception: Can't open file") 
                else:
                    print("Black list generation:")
                    for bl in Fbl:
                        bl = bl.strip().lower()
                        if re.search(r'[a-z]',bl):
                            lemma_bl = bl
                        else:
                            lemma_bl  = getLemma(bl)
                        print("raw: %s normal_form:%s" % (bl, lemma_bl))
                        if lemma_bl not in BL:  BL.append(lemma_bl)
                    Fbl.close()
                    for bl in BL:
                        print(bl)
                

            Fin.seek(0)
            current_line = 0
            for line in Fin:
                current_line +=1
                print("Analyze line: %d of %d\r" % (current_line,INFO['total_lines']))

                mode = int(sys.argv[1])
                INFO['mode']=mode
                if mode==1:    INFO['analyzed_words'] += tta_module_1w.proceed(getWords(line), W, BL) ## Анализируем по 1 слову в строке , Если BL опустить то  без блеклиста.
                elif mode==2: INFO['analyzed_words'] += tta_module_2w.proceed(getWords(line), W, BL) ## Анализируем по 2 слова строке , Если BL опустить то  без блеклиста.
                elif mode==3: INFO['analyzed_words'] += tta_module_3w.proceed(getWords(line), W, BL) ## Анализируем по 3 слова строке , Если BL опустить то  без блеклиста.
                elif mode==4: INFO['analyzed_words'] += tta_module_4w.proceed(getWords(line), W, BL) ## Анализируем по 4 слова строке , Если BL опустить то  без блеклиста.

            Fin.close()
            for p in INFO:
                print(' '.join((p,str(INFO[p])))+'\n')
            print("Sorting and write output to file...")
            list_W = list(W.items())
            list_W.sort(key=lambda i: i[1], reverse=True )
            W = list_W
            for p in list_W:
                Fout.write(';'.join((p[0],str(p[1]),str(p[1]*100/INFO['analyzed_words'])))+'\n')
            print("Done")
                
            Fout.close()


        
    
if __name__ == "__main__":  main()
