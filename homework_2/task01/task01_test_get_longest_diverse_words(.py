from typing import List

import pytest
from task01 import get_longest_diverse_words


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
