#!/usr/bin/env python3
import sys
import string
from collections import defaultdict

def load_codes(code_file):
    codes = {}
    with open(code_file, "r") as file:
        for line in file:
            code, word = line.strip().split('\t')
            codes[word] = int(code)
    return codes

def load_idf(code_file):
    idf = {}
    with open(code_file, "r") as file:
        for line in file:
            code, df = line.strip().split('\t')
            idf[int(code)] = int(df)
    return idf

def mapper():
    codes = load_codes('/home/moaz/output1.txt')
    idf = load_idf('/home/moaz/output4.txt')
    article_dict = defaultdict(int)

    for line in sys.stdin:
        line = line.strip()
        words = line.lower().translate(str.maketrans('', '', string.punctuation)).split()
        for word in words:
            code = codes.get(word)
            if code:
                article_dict[code] += 1
    
    for code,value in article_dict.items():
        idf_val = idf.get(code)
        if idf_val and idf_val!=0:
            article_dict[code] = value / idf_val
        else:
            article_dict[code] = value

        print(f'{code}\t{article_dict[code]}')

if __name__ == "__main__":
    mapper()

