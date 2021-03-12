"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""

import string
from collections import defaultdict
from typing import List


def read_file(file_path: str) -> str:
    with open(file_path, "r") as data:
        return bytes(data.read(), "ascii").decode("unicode-escape")


def get_longest_diverse_words(file_path: str) -> List[str]:
    text = read_file(file_path)
    text = "".join(char for char in text if char not in set(string.punctuation))
    word_list = text.split()
    word_list = sorted(word_list, key=lambda x: (-len(set(x)), -len(x)))
    return word_list[:10]


def get_rarest_char(file_path: str) -> str:
    dict_char = defaultdict(int)
    text = read_file(file_path)
    for symbol in text:
        dict_char[symbol] += 1
    return min(dict_char, key=dict_char.get)


def count_punctuation_chars(file_path: str) -> int:
    count_punctuation_char = 0
    text = read_file(file_path)
    for chars in text:
        if chars in string.punctuation:
            count_punctuation_char += 1
    return count_punctuation_char


def count_non_ascii_chars(file_path: str) -> int:
    count_non_ascii_char = 0
    text = read_file(file_path)
    for non_ascii_char in text:
        if ord(non_ascii_char) > 128:
            count_non_ascii_char += 1
    return count_non_ascii_char


def get_most_common_non_ascii_char(file_path: str) -> str:
    dict_non_ascii_char = defaultdict(int)
    text = read_file(file_path)
    for non_ascii_char in text:
        if ord(non_ascii_char) > 128:
            dict_non_ascii_char[non_ascii_char] += 1
    return max(dict_non_ascii_char, key=dict_non_ascii_char.get)
