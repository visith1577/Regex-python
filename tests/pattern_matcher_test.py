import pattern_matcher
import pytest


# all possible test cases written using pytest
@pytest.mark.parametrize(
    "txt,pat,expected",
    [
        ('abcdefa', 'a|c', True),
        ('abcdefa', 'a|k', True),
        ('abde', '^a|b', True),
        ('abde', '^a|k', True),
        ('abde', '^d|b', True),
        ('abde', 'e$|d', True),
        ('abde', 'e$|s', True),
        ('abde', 's$|b', True),
        ('abde', 'c|a', True),
        ('abcdefa', 'n|m', False),
        ('abde', '^c|n', False),
        ('abde', '^b|^k', False),
        ('abde', 'a$|n', False),
        ('abde', 'a$|b$', False),
        ('abde', 'k|s$', False),
        ('abcd', '^a', True),
        ('abcd', 'e$', True),
    ]
)
def test_pattern(txt, pat, expected):
    assert pattern_matcher.matcher(txt, pat) == expected
