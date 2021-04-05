"""
We have a file that works as key-value storage, each like is represented as key and value separated by = symbol, example:

name=kek
last_name=top
song_name=shadilay
power=9001

Values can be strings or integer numbers. If a value can be treated both as a number and a string, it is treated as number.

Write a wrapper class for this key value storage that works like this:

storage = KeyValueStorage('path_to_file.txt')
that has its keys and values accessible as collection items and as attributes.
Example:
storage['name']  # will be string 'kek'
storage.song_name  # will be 'shadilay'
storage.power  # will be integer 9001

In case of attribute clash existing built-in attributes take precedence.
In case when value cannot be assigned to an attribute (for example when there's a line `1=something`) ValueError should be raised.
File size is expected to be small, you are permitted to read it entirely into memory.
"""


from keyword import iskeyword


class KeyValueStorage:
    def __init__(self, file_path: str):
        self.storage = {}

        with open(file_path, "r") as file:
            for line in file:
                key, value = line.rstrip().split("=")
                if not key.isidentifier() or iskeyword(key):
                    raise ValueError("This key cannot be assigned to an attribute.")
                value = int(value) if value.isnumeric() else value
                self.storage[key] = value

    def __getitem__(self, item):
        return self.storage[item]

    def __getattr__(self, item):
        return self.storage[item]
