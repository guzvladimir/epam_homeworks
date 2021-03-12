from typing import List

import pytest

from task01.task01 import (  # isort: skip
    count_punctuation_chars,
    count_non_ascii_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        (
            "data_test01_1.txt",
            [
                "Zahlenverhältnis",
                "ausgerichtet",
                "Unterschied",
                "Entwicklung",
                "Darstellung",
                "auszeichnet",
                "Rechtsraum",
                "Wahlvorgang",
                "Auswertung",
                "Willensakt",
            ],
        ),
        (
            "data_test01_2.txt",
            [
                "Überschreitung",
                "überwirklichen",
                "Todesfurcht",
                "Überwindung",
                "Überwindung",
                "Grundfrage",
                "Lebenshort",
                "erschließt",
                "Schreckens",
                "Todesgang",
            ],
        ),
    ],
)
def test_get_longest_diverse_words(file_path: str, expected_result: List[str]):
    assert get_longest_diverse_words(file_path) == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [("data_test01_1.txt", "U"), ("data_test01_2.txt", "z")],
)
def test_get_rarest_char(file_path: str, expected_result: str):
    assert get_rarest_char(file_path) == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [("data_test01_1.txt", 14), ("data_test01_2.txt", 9)],
)
def test_count_punctuation_chars(file_path: str, expected_result: int):
    assert count_punctuation_chars(file_path) == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [("data_test01_1.txt", 9), ("data_test01_2.txt", 11)],
)
def test_count_non_ascii_chars(file_path: str, expected_result: int):
    assert count_non_ascii_chars(file_path) == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [("data_test01_1.txt", "ä"), ("data_test01_2.txt", "Ü")],
)
def test_get_most_common_non_ascii_char(file_path: str, expected_result: str):
    assert get_most_common_non_ascii_char(file_path) == expected_result
