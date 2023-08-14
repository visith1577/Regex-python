from typing import List
from kmp_algorithm import match_regex_bool
from reg_cmds import pipe, end, begin
from helper import pipe_checker


def matcher(txt: str, pat: str) -> bool:
    result = []
    pat = pat.replace(" ", "")

    # if | in pattern but not ^ or $
    if pat.rfind('|') != -1 and pat.rfind('^') == -1 and pat.rfind('$') == -1:

        pattern_list = pipe(pat)
        # print(pattern_list)

        for pat in pattern_list:
            result.append(match_regex_bool(txt, pat))

        if pipe_checker(result):
            result = [True]

    # if | in pattern and ^ or $
    elif pat.rfind('|') != -1 and (pat.rfind('^') != -1 or pat.rfind('$') != -1):
        pattern_list = pipe(pat)
        # print(pattern_list)

        for pat in pattern_list:
            result.append(match_regex_bool(txt, pat))
            res_begin = begin(txt, pat)
            res_end = end(txt, pat)
            if res_begin is not None:
                result.append(res_begin)
            if res_end is not None:
                result.append(res_end)

        if pipe_checker(result):
            result = [True]

    # if ^ in pattern
    elif begin(txt, pat) is not None:
        res_begin = begin(txt, pat)
        result.append(res_begin)

    # if $ in pattern
    elif end(txt, pat) is not None:
        res_end = end(txt, pat)
        result.append(res_end)

    # print(result)
    return all(result)


# same as matcher function but iterates through several words
# matcher for cases with more than one word
def matcher_iter(text: str, pat: str):
    text_arr = text.split()
    # print(text_arr)
    result = []

    for word in text_arr:
        # print(word)
        res = matcher(word, pat)
        result.append(res)

    return result
