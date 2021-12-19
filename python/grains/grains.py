def square(number: int):
    if 0 < number <= 64:
        return 2 ** (number - 1)
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    return sum(square(i) for i in range(1, 65))
