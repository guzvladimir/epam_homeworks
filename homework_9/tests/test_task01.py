from task01.task01 import merge_sorted_files


def test_merge_sorted_files_same_length():
    assert list(merge_sorted_files(["file1.txt", "file2.txt"])) == [1, 2, 3, 4, 5, 6]


def test_merge_sorted_files_different_length():
    assert list(merge_sorted_files(["file2.txt", "file3.txt"])) == [
        -11,
        0,
        2,
        4,
        6,
        9,
        10,
        12,
        13,
    ]


def test_merge_sorted_files_with_empty_file():
    assert list(merge_sorted_files(["file1.txt", "file4.txt"])) == [1, 3, 5]
