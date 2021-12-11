from functools import reduce, map
from typing import Iterable


def flatten(iterable: Iterable) -> Iterable:
    """Take a nested list and return a single flattened list with all values except nil/null."""

    
    while iterable:
        _item = iterable.pop()
        if type(_item) is not list:
            output.insert(0, _item)
        else:
            output = output[::]
            flatten(_item, output)

    return output

