#!/usr/bin/env python3
import sys
from collections import defaultdict

def load_weights(code_file):
    dict_out = {}
    with open(code_file, "r") as file:
        for line in file:
            article_num, remaining_text = line.split("\t(", 1)
            article_num = int(article_num) 
            remaining_text = remaining_text[:-2]
            code_value_pairs = remaining_text.split("), (")
            inner_dict = {}  
            for pair in code_value_pairs:
                code, value = pair.split(":")
                inner_dict[int(code)] = float(value)
            dict_out[article_num] = inner_dict
    return dict_out


def reducer():
    weights = load_weights('/home/moaz/output3.txt')
    query_dict = defaultdict(float)
    for line in sys.stdin:
        line = line.strip()
        code, weight = line.split('\t')
        query_dict[int(code)] = float(weight)
    
    for id, value in weights.items():
        matching = 0.0
        for code, weight in query_dict.items():
            if code in weights[id]:
                matching += weight * weights[id][code]
        if matching > 0.0:
            print(f'Article : {id}\t Relevance : {matching}')

if __name__ == "__main__":
    reducer()
