import pytest
from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_all_positive():
    assert longest_positive_streak([1, 2, 3]) == 3

def test_mixed_with_negatives_and_zero():
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_multiple_streaks():
    # Two streaks: [1, 2] (len 2) and [4, 5, 6] (len 3)
    assert longest_positive_streak([1, 2, 0, -3, 4, 5, 6]) == 3

def test_all_non_positive():
    assert longest_positive_streak([0, -1, -2]) == 0
