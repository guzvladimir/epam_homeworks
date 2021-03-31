"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


def find_occurrences(tree: dict, element: Any) -> int:
    def counter(values, element):
        element_counter = 0
        for item in values:
            if isinstance(item, (int, str, bool)):
                element_counter += 1 if item is element else 0
            elif not isinstance(item, dict):
                element_counter += counter(item, element)
            else:
                element_counter += counter(item.values(), element)
        return element_counter

    return counter(tree.values(), element)


if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))  # 6
