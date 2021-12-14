from typing import Iterable


def flatten(nested_list: Iterable) -> Iterable:
    """Take a nested list and return a single flattened list with all values except nil/null."""
    return [element for element in flatten_list(nested_list)]


def flatten_list(nested_list: Iterable) -> Iterable:
    for element in nested_list:
        if isinstance(element, list):
            yield from flatten_list(element)
        elif element is not None and not isinstance(element, tuple):
            yield element
