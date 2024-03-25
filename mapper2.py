#!/usr/bin/env python3
import sys
import string

def load_codes(code_file):
    codes = {}
    with open(code_file, "r") as file:
        for line in file:
            code, word = line.strip().split('\t')
            codes[word] = int(code)
    return codes

def mapper():
    # Load the codes
    codes = load_codes('/inputs/output_sample/part-00000')

    for line in sys.stdin:
        columns = line.strip().split(',')
        # If there are less than 4 columns, skip this line
        if len(columns) < 4:
            continue

        words = columns[3].lower().translate(str.maketrans('', '', string.punctuation)).split()
        article_dict = dict.fromkeys(codes.values(), 0)

        for word in words:
            code = codes.get(word)
            if code:
                article_dict[code] += 1

        print(f"{columns[0]}{article_dict}")

if __name__ == "__main__":
    mapper()
