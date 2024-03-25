#!/usr/bin/env python3
import sys

def reducer():
    current_article = None
    current_counts = {}

    for line in sys.stdin:
        article_id, counts_str = line.strip().split('{', 1)
        counts_str = counts_str.rstrip("}")
        counts = {}

        for item in counts_str.split(', '):
            key, value = map(int, item.split(': '))
            counts[key] = value

        if current_article == article_id:
            for code, count in counts.items():
                current_counts[code] = current_counts.get(code, 0) + count
        else:
            if current_article:
                print_tuples(current_article, current_counts)
            current_article = article_id
            current_counts = counts

    # Output the last article's tuples
    if current_article:
        print_tuples(current_article, current_counts)

def print_tuples(article_id, counts):
    # Print only non-zero counts
    print(article_id)
    for code, count in counts.items():
        if count > 0:
            print(f"({code}, {count})")

if __name__ == "__main__":
    reducer()
