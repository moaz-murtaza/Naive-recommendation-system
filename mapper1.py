#!/usr/bin/env python3
import sys
import string
import csv

def mapper():
    lines = csv.reader(sys.stdin)

    for columns in lines:
        if len(columns) < 4:
            continue

        words = columns[3].lower().translate(str.maketrans('', '', string.punctuation)).split() 
        for word in words:
            print(f"{word}\t1")

if __name__ == "__main__":
    mapper()

