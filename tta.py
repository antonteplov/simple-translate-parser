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

MIN_WORD_LEN = 3

INFO = {
    'filename': "",
    'total_lines': 0,
    'total_raw_words': 0,
    'analyzed_words':0

    }

W ={}  

BL = []




def getLemma(w):    
     morph = pymorphy2.MorphAnalyzer()
     p = morph.parse(w)[0]
     return p.normal_form    

def GetWord(line):
    
    line = re.sub(r"[#%!@*,.;:?(){}_/]", "", line)  #удаляем ненужные симоволы
    line = re.sub(r"\s+"," ",line)  # удаляем лишние пробелы
    line = line.strip() #удаляем символы пробелов в начале и конце строки
    line = line.lower()
    return line.split(' ')


def main():
    if len(sys.argv) < 3:
        print ("Teplov Text Analyzer (TTA) v%s" % 1)
        print ("Use %s <input file> <output file> [blacklist file]" % (sys.argv[0]))
        print ("Input file содержит текстовые строки - одна строка , одна фраза для анализа\n Output file  будет содержать отчет о выполненной работе в формате CSV. Слова будут приведены в нормальную форму и проведен подсет вхождений такий простых слов.\n В качестве необезательного параметра можно указать имя файла blacklist. В этом файле одна строка=одно слово, которое будет исключаться из анализа.")
        exit()
    print ("Try open input file %s" % (sys.argv[1]) )
    try:
        Fin = open(sys.argv[1])
    except:
        print("Exception: Can't open file")
    else:
        print("Try open output file %s" % (sys.argv[2]) )
        try:
            Fout = open(sys.argv[2],'w')
        except:
            print("Exception: Can't open file") 
        else:
            INFO['filename'] = sys.argv[1]
            for line in Fin:
                INFO['total_lines'] +=1
                print(line)
                for word in GetWord(line):
                    #print("{%s} %d",word,len(word))
                    INFO['total_raw_words'] +=1
            
            if len(sys.argv) == 4:
                print("Try open black list file %s" % (sys.argv[3]) )
                try:
                    Fbl = open(sys.argv[3])
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
                for word in GetWord(line):
                    
                    if len(word) >= MIN_WORD_LEN:
                        #print("%s %d" % (word , len(word)))
                        INFO['analyzed_words'] +=1
                        word = getLemma(word)
                        if word not in BL:
                            if word in W:
                                W[word] += 1
                            else:
                                W[word]=1

            Fin.close()
            for p in INFO:
                Fout.write(';'.join((p,str(INFO[p])))+'\n')
            for p in W:
                Fout.write(';'.join((p,str(W[p])))+'\n')
                
            Fout.close()


        
    
if __name__ == "__main__":  main()
