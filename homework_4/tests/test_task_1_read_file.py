import os

import pytest
from task01.task_1_read_file import read_magic_number


@pytest.fixture()
def create_temp_file(temp_file, value):
    with open(temp_file, "w") as file:
        file.write(value)


@pytest.mark.parametrize(
    ["temp_file", "value"],
    [
        ("data1.txt", "1"),
        ("data2.txt", "2"),
        ("data3.txt", "2.5\n3\n4\n"),
    ],
)
def test_read_magic_number_true(temp_file, value, create_temp_file):
    actual_result = read_magic_number(temp_file)
    os.remove(temp_file)
    assert actual_result is True


@pytest.mark.parametrize(
    ["temp_file", "value"],
    [
        ("data1.txt", "-1"),
        ("data2.txt", "0"),
        ("data3.txt", "3\n2\n1\n"),
        ("data4.txt", "0.99\n"),
    ],
)
def test_read_magic_number_false(temp_file, value, create_temp_file):
    actual_result = read_magic_number(temp_file)
    os.remove(temp_file)
    assert actual_result is False


@pytest.mark.parametrize(
    ["temp_file", "value"],
    [
        ("data1.txt", "error"),
        ("data2.txt", ""),
        ("data3.txt", "2value"),
    ],
)
def test_read_magic_number_value_error(temp_file, value, create_temp_file):
    with pytest.raises(ValueError):
        read_magic_number(temp_file)
    os.remove(temp_file)
