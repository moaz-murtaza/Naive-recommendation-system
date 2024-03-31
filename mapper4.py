#!/usr/bin/env python3
import sys
import string
from collections import defaultdict

def hash_code(word):
    return abs(hash(word)) % (10 ** 6)

def load_idf(code_file):
    idf = {}
    with open(code_file, "r") as file:
        for line in file:
            code, df = line.strip().split('\t')
            idf[int(code)] = int(df)
    return idf

def mapper():
    idf = load_idf('/home/bilal/output4.txt')
    article_dict = defaultdict(int)

    for line in sys.stdin:
        line = line.strip()
        words = line.lower().translate(str.maketrans('', '', string.punctuation)).split()
        for word in words:
            code = hash_code(word)
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



