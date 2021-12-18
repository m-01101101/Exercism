from typing import List, Dict, Tuple
from collections import Counter


def create_inventory(items: List[str]) -> Counter:
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """

    return Counter(items)


def add_items(inventory: Dict[str, int], items: List[str]) -> Dict[str, int]:
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """

    _update = Counter(items)
    _new = {k: v for k, v in _update.items() if k not in inventory}
    _updated = {k: v + _update[k] for k, v in inventory.items() if k in items}
    _unchanged = {k: v for k, v in inventory.items() if k not in items}
    return _new | _updated | _unchanged


def decrement_items(inventory: Dict[str, int], items: List[str]) -> Dict[str, int]:
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """
    _remove = Counter(items)
    _removed = {k: v - _remove[k] for k, v in inventory.items() if k in items}
    _unchanged = {k: v for k, v in inventory.items() if k not in items}
    final = _removed | _unchanged
    return {k: max(v, 0) for k, v in final.items()}


def remove_item(inventory: Dict[str, int], item: str) -> Dict[str, int]:
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """
    inventory.pop(item) if item in inventory else inventory
    return inventory


def list_inventory(inventory: Dict[str, int]) -> List[Tuple[str, int]]:
    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    return [(k, v) for k, v in inventory.items() if v > 0]
