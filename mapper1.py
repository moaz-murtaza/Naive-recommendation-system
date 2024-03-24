#!/usr/bin/env python3
import sys
import string

def mapper():
    for line in sys.stdin:
        columns = line.strip().split(',')
        # If there are less than 4 columns, skip this line
        if len(columns) < 4:
            continue
        words = columns[3].lower().translate(str.maketrans('', '', string.punctuation)).split()
        for word in words:
            print(f"{word}\t1")

if __name__ == "__main__":
    mapper()

