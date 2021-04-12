"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6

"""
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    count_lines_tokens = 0
    for file_name in dir_path.glob("*." + file_extension):
        with open(file_name, "r") as file:
            if tokenizer:
                for line in file.readlines():
                    count_lines_tokens += len(tokenizer(line))
            else:
                count_lines_tokens += sum(1 for _ in file.readlines())
    return count_lines_tokens
