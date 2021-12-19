from typing import List


def is_suitable_triangle(sides: List[int]) -> bool:
    # test require return false, would prefer to raise ValueError
    assert len(sides) == 3, ValueError("Too many sides")
    sides.sort()
    if sides[-1] == 0:
        return False

    elif min(sides) + sides[1] <= max(sides):
        return False

    else:
        return True


def equilateral(sides: List[int]) -> bool:
    return bool(is_suitable_triangle(sides) and len(set(sides)) == 1)


def isosceles(sides: List[int]) -> bool:
    return bool(is_suitable_triangle(sides) and len(set(sides)) <= 2)


def scalene(sides: List[int]) -> bool:
    return bool(is_suitable_triangle(sides) and len(set(sides)) == 3)
