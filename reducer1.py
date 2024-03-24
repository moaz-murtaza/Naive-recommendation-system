#!/usr/bin/env python3

import sys

def reducer():
    current_word = None
    word_count = 0
    vocab = {}
    
    for line in sys.stdin:
        word, count = line.strip().split('\t')
        
        count = int(count)
        
        if current_word == word:
            word_count += count
        else:
            if current_word:
                vocab[current_word] = len(vocab)
            current_word = word
            word_count = count
    
    if current_word:
        vocab[current_word] = len(vocab)
    
    for word, index in vocab.items():
        print(f"{index}\t{word}")

if __name__ == "__main__":
    reducer()

