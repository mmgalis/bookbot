#import numpy as np
from collections import Counter, defaultdict
import os

def main():
    book = "frankenstein.txt"
    book_path = os.path.join("books", book)
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    letter_dict = get_letter_dict(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(num_words, "words found in the document")
    print("")
    for w in sorted(letter_dict, key=letter_dict.get, reverse=True):
        print("The", w, "character was found", letter_dict[w], "times")
    print("--- End report ---")

def get_num_words(string):
    words = string.split()
    nr_of_words = len(words)
    return nr_of_words

def get_chars_dict(string):
    lowered_string = string.lower()
    chars = {}
    for c in lowered_string:
        if c in chars:
            chars[c] += 1
        else: 
            chars[c] = 1
    return chars

def get_letter_dict(string):
    lowered_string = string.lower()
    chars = {}
    for c in lowered_string:
        if c.isalpha():
            if c in chars:
                chars[c] += 1
            else: 
                chars[c] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()





