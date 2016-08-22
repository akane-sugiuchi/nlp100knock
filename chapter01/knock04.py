# -*- coding: utf-8 -*-
s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
s = s.replace('.', "")
s = s.replace(',', "")
s = s.split()

index_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dict = {}

for i,w in enumerate(s):
    index = 1 if i+1 in index_list else 2
    dict[w[:index:1]] = i+1
print (dict)

