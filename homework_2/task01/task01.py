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


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path, "r") as data:
        text = bytes(data.read(), "ascii").decode("unicode-escape")
        text = "".join(char for char in text if char not in set(string.punctuation))
        word_list = text.split()
        word_list = sorted(word_list, key=lambda x: (-len(set(x)), -len(x)))
    return word_list[:10]


def get_rarest_char(file_path: str) -> str:
    dict_char = defaultdict(int)
    with open(file_path, "r") as data:
        text = bytes(data.read(), "ascii").decode("unicode-escape")
        for symbol in text:
            dict_char[symbol] += 1
    return min(dict_char, key=dict_char.get)


def count_punctuation_chars(file_path: str) -> int:
    char = 0
    with open(file_path, "r") as data:
        text = bytes(data.read(), "ascii").decode("unicode-escape")
        for chars in text:
            if chars in string.punctuation:
                char += 1
    return char


def count_non_ascii_chars(file_path: str) -> int:
    non_ascii = 0
    with open(file_path, "r") as data:
        text = bytes(data.read(), "ascii").decode("unicode-escape")
        for char in text:
            if ord(char) > 128:
                non_ascii += 1
    return non_ascii


def get_most_common_non_ascii_char(file_path: str) -> str:
    dict_ascii_char = defaultdict(int)
    with open(file_path, "r") as data:
        text = bytes(data.read(), "ascii").decode("unicode-escape")
        for symbol in text:
            if ord(symbol) > 128:
                dict_ascii_char[symbol] += 1
    return max(dict_ascii_char, key=dict_ascii_char.get)
