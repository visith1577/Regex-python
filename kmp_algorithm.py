from typing import List

"""
code for KMP algorithm: KMP table and pattern matcher with index output and bool output
"""


def match_regex_bool(text: str, pattern: str) -> bool:
    """
    Matches the given pattern in the text using the KMP algorithm.
    :param text : text string
    :param pattern : regex pattern to identify
    :return: bool value of if pattern exists
    """
    N = len(text)
    M = len(pattern)
    table = [0] * M

    j = 0

    kmp_table(pattern, M, table)

    i = 0

    while (N - i) >= (M - j):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == M:
            break
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = table[j - 1]
            else:
                i += 1

    return j == len(pattern)


def match_regex(text: str, pattern: str) -> List[int]:
    """
    Matches the given pattern in the text using the KMP algorithm.
    :param text : text string
    :param pattern : regex pattern to identify
    :return: list of integers containing indexOf matched pattern
    """
    index_list = []
    N = len(text)
    M = len(pattern)
    table = [0] * M

    j = 0

    kmp_table(pattern, M, table)

    i = 0

    while (N - i) >= (M - j):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == M:
            index_list.append(i - j)
            j = table[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = table[j - 1]
            else:
                i += 1

    return index_list


def kmp_table(pat: str, n: int, table: List[int]):
    """Creates a table for the KMP algorithm."""
    i = 1
    j = 0
    while i < n:
        if pat[i] == pat[j]:
            j += 1
            table[i] = j
            i += 1
        else:
            if j != 0:
                j = table[j - 1]
            else:
                table[i] = 0
                i += 1
    return table
