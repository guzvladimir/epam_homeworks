from task01.task01 import find_occurrences

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", 12, "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "smth": True,
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": [True, "lot", "of", 12, {"nested_key": ["RED", 12]}],
        },
    },
    "fourth": "RED",
}


def test_find_occurrences():
    assert find_occurrences(example_tree, "RED") == 6
    assert find_occurrences(example_tree, "BLUE") == 2
    assert find_occurrences(example_tree, True) == 2
    assert find_occurrences(example_tree, 12) == 3
