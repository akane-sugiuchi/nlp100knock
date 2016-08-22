# -*- coding: utf-8 -*-
import json
from knock20 import extract_str

file_name = 'jawiki-country.json'
str = "イギリス"
lines = extract_str(file_name, str).split("\n")

for line in lines:
    if "Category" in line:
        print (line)

