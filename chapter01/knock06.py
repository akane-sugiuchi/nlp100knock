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

str_x = "paraparaparadise"
str_y = "paragraph"
X = set(ngram(str_x,2, "str"))
Y = set(ngram(str_y,2, "str"))

print (X.union(Y))         # 和集合
print (X.intersection(Y))  # 積集合
print (X.difference(Y))    # 差集合

print ("se" in X)
print ("se" in Y)
