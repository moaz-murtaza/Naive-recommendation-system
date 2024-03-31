#!/usr/bin/env python3
import sys
import string

def hash_code(word):
    return abs(hash(word)) % (10 ** 6)

def mapper():

    next(sys.stdin)
    for line in sys.stdin:
        columns = line.strip().split(',')
        # If there are less than 4 columns, skip this line
        if len(columns) < 4:
            continue

        words = columns[3].lower().translate(str.maketrans('', '', string.punctuation)).split()
        article_dict = {}

        for word in words:
            code = hash_code(word)
            if code not in article_dict:
                article_dict[code] = 1
            else:
                article_dict[code] += 1

        print(f"{columns[0]}{article_dict}")

if __name__ == "__main__":
    mapper()
