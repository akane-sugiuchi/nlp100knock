# -*- coding: utf-8 -*-
import json

def extract_str(file_name, str):
    lines = ""
    with open(file_name, encoding='utf-8') as f:
        a_json = f.readline()
        while a_json:
            a_dict = json.loads(a_json)
            if a_dict["title"] == str:
                lines = lines + a_dict["text"]
            a_json = f.readline()
    return lines

if __name__ == "__main__":
    file_name = 'jawiki-country.json'
    str = "イギリス"
    lines = extract_str(file_name, str)
    print (lines)

