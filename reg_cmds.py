from kmp_algorithm import match_regex, match_regex_bool
from helper import loop_indexes
from typing import List


def pipe(pat: str) -> List[str]:
    """
    contains base logic for '|' regex patter
    :param pat:
    :return: list containing patterns to be matched
    """
    print("found |")

    index_list = loop_indexes(pat, '|')

    print("index list: ", index_list)
    pattern_list = []  # list containing expressions within |
    start_in = 0
    for index in index_list:
        if index > start_in:
            pattern_list.append(pat[start_in:index])
            start_in = index + 1
    pattern_list.append(pat[start_in:])

    return pattern_list


def end(txt: str, pat: str):
    """
    logic for '$' regex
    :param txt:
    :param pat:
    :return: bool value of if txt ends with pat
    """
    result = None
    if pat.rfind('$') != -1:

        print("found $")

        pat_ = pat[:-1]
        # print(pat_)

        if match_regex_bool(txt, pat_):
            index = match_regex(txt, pat_)[-1]
            # print(index)

            # print(len(txt) - len(pat_))

            if index == len(txt) - len(pat_):
                result = True
            else:
                result = False
        else:
            return result
    else:
        return result

    return result


def begin(txt: str, pat: str):
    """
    logic for '^' regex
    :param txt:
    :param pat:
    :return: bool value of if txt begin with pat
    """
    result = None
    if pat.rfind('^') != -1:

        print("found ^")

        pat_ = pat[1:]
        # print(pat_)

        if match_regex_bool(txt, pat_):
            index = match_regex(txt, pat_)[0]
            print("index :", index)
            if index == 0:
                result = True
            else:
                result = False
        else:
            return result
    else:
        return result

    return result

