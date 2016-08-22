# -*- coding: utf-8 -*-
s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
s = s.replace('.', "")
s = s.replace(',', "")
s = s.split()

list = []

for w in s:
    list.append(len(w))
print (list)

