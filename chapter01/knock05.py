# -*- coding: utf-8 -*-

def ngram(s,n, type):
    words = []
    s = s.replace('.', "")
    s = s.replace(',', "")
    if type == "str":
        #s = ''.join(s)
        s = s.replace(' ', '')
    else:
        s = s.split()
    for i in range(0, len(s)-n+1):
        words.append(s[i:i+n:1])
    return words


s = "I am an NLPer"
print (ngram(s,2, "word"))
s.split()
print(ngram(s,2, "str"))
