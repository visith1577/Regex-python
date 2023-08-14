from typing import List


def loop_indexes(pat: str, sym: str) -> List[int]:
    """loop through indexes of a list"""
    start = 0

    indexes = []

    while start < len(pat):
        start = pat.find(sym, start)
        if start == -1:
            break
        indexes.append(start)
        start += 1

    return indexes


def pipe_checker(result: List[bool]) -> bool:
    """Validate result of | regex"""
    return any(result)
