#!/usr/bin/env python3
import sys
from collections import defaultdict

def reducer():
    # Variables to store articles and document frequencies
    article_data = defaultdict(dict)
    df_counts = defaultdict(int)


    # Read input from mapper
    for line in sys.stdin:
        line = line.strip()

        # Split article id from its counts
        article_id, counts_str = line.split('{', 1)
        article_id = int(article_id)


        counts_pairs = counts_str.rstrip('}').split(', ')

        for pair in counts_pairs:
            data = pair.split(':')
                
            if len(data) != 2: 
                continue
                
            code, count = map(int, data)
            article_data[article_id][code] = count
            df_counts[code] += 1
            
    for article_id, counts in article_data.items():
        for code, count in counts.items():
            print(f"{code}\t{df_counts[code]}")
            
    
if __name__ == "__main__":
    reducer()
