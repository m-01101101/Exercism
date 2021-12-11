from typing import List


def round_scores(student_scores: List[float]) -> List[int]:
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """

    return [round(score) for score in student_scores]


def count_failed_students(student_scores: List[int]) -> int:
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """

    return len([score for score in student_scores if score <= 40])


def above_threshold(student_scores: List[int], threshold: int) -> List[int]:
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest: int) -> List[int]:
    """
    :param highest: integer of highest exam score.
    :return: list of integer lower threshold scores for each D-A letter grade interval.
             For example, where the highest score is 100, and failing is <= 40,
             The result would be [41, 56, 71, 86]:

             41 <= "D" <= 55
             56 <= "C" <= 70
             71 <= "B" <= 85
             86 <= "A" <= 100
    """
    increment = (highest - 40) // 4
    min_d = 41  # always true
    min_c = min_d + increment
    min_b = min_c + increment
    min_a = min_b + increment

    return [min_d, min_c, min_b, min_a]


def student_ranking(student_scores: List[int], student_names: List[str]) -> List[int]:
    """
    :param student_scores: list of scores in descending order.
    :param student_names: list of names in descending order by exam score.
    :return: list of strings in format ["<rank>. <student name>: <score>"].
    """

    return [
        f"{idx + 1}. {student[0]}: {student[1]}"
        for idx, student in enumerate(zip(student_names, student_scores))
    ]


def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    _result = [i for i in student_info if i[1] == 100]

    return _result if not _result else _result[0]
