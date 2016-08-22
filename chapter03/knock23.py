# -*- coding: utf-8 -*-
import re
from knock20 import extract_str

file_name = 'jawiki-country.json'
str = "イギリス"
lines = extract_str(file_name, str).split("\n")

for line in lines:
    category_line = re.search("^\[\[Category:(.*?)(|\|.*)\]\]$", line)
    if category_line:
        print (category_line.group(1))

