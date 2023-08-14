import pytest
import pattern_matcher


# check if iterator functions
@pytest.mark.parametrize(
    "txt,pat,expected",
    [
        ('abcdef', '^a|e$', [True]),
        ('abcdef abceds kghtm', 'a|b', [True, True, False])
    ]
)
def test_pattern(txt, pat, expected):
    assert pattern_matcher.matcher_iter(txt, pat) == expected
