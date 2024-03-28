#!/usr/bin/env python3
import sys
import string
import csv

def load_codes(code_file):
    codes = {}
    with open(code_file, "r") as file:
        for line in file:
            code, word = line.strip().split('\t')
            codes[word] = int(code)
    return codes

def mapper():
    codes = load_codes('/home/moaz/output1.txt')
    articles = dict()

    lines = csv.reader(sys.stdin)

    for columns in lines:
        if len(columns) < 4:
            continue

        words = columns[3].lower().translate(str.maketrans('', '', string.punctuation)).split() 
        article_id = columns[0]

        if not articles.get(article_id):
            articles[article_id] = dict.fromkeys(codes.values(), 0)

        article_dict = articles[article_id]
        
        for word in words:
            code = codes.get(word)
            if code:
                article_dict[code] += 1

    # Print results for all articles
    for article_id, word_frequencies in articles.items():
        print(f"{article_id}{word_frequencies}") 

if __name__ == "__main__":
    mapper()
