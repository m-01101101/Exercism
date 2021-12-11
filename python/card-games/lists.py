from typing import List


def get_rounds(number: int) -> List[int]:
    """

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1: List[int], rounds_2: List[int]) -> List[int]:
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds: List[int], number: int) -> bool:
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """

    return len([i for i in rounds if i == number]) > 0


def card_average(hand: List[int]) -> float:
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand: List[int]) -> bool:
    """

    :param hand: list - cards in hand.
    :return: bool - is approximate average the same as true average?
    """
    sorted(hand)

    approx_avg1 = hand[len(hand) // 2]
    approx_avg2 = (hand[0] + hand[-1]) / 2
    return approx_avg1 == card_average(hand) or approx_avg2 == card_average(hand)


def average_even_is_average_odd(hand: List[int]) -> bool:
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    evens = [n for i, n in enumerate(hand) if i % 2 == 0]
    odds = [n for i, n in enumerate(hand) if i % 2 == 1]

    return card_average(evens) == card_average(odds)


def maybe_double_last(hand: List[int]) -> List[int]:
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    return hand[:-1] + [22] if hand[-1] == 11 else hand
