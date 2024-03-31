#!/usr/bin/env python3
import sys

def mapper():
    current_article = None
    current_counts = {}

    for line in sys.stdin:
        line = line.strip()

        if line.isdigit():  # Start of a new article block detection
            if current_article:
                print_article(current_article, current_counts)
            current_article = int(line)
            current_counts.clear()
            continue

        # Interpret lines as tuples (code, count)
        code, count = map(int, line.strip('()').split(', '))
        current_counts[code] = current_counts.get(code, 0) + count

    # Output the last article's counts
    if current_article:
        print_article(current_article, current_counts)

def print_article(article_id, counts):
    # Format counts dictionary into string
    counts_str = ', '.join(f"{code}:{count}" for code, count in counts.items())
    print(f"{article_id}{{{counts_str}}}")

if __name__ == "__main__":
    mapper()

