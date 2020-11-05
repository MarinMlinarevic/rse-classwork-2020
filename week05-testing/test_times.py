from times import *
from pytest import raises

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_no_overlap():
    first = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    second = time_range("2011-01-12 10:00:00", "2011-01-12 12:00:00")
    result = compute_overlap_time(first, second)
    expected = []
    assert result == expected

def test_both_several_intervals():
    first = time_range("2010-01-12 10:31:00", "2010-01-12 12:36:00", 2, 60)
    second = time_range("2010-01-12 10:30:00", "2010-01-12 10:35:00", 2, 60)
    result = compute_overlap_time(first, second)
    expected = [("2010-01-12 10:31:00", "2010-01-12 10:32:00"), ("2010-01-12 10:33:00","2010-01-12 10:35:00")]
    assert result == expected

def test_one_starts_when_other_ends():
    first = time_range("2010-01-12 10:31:00", "2010-01-12 12:36:00")
    second = time_range("2010-01-12 12:36:00", "2010-01-12 12:40:00")
    result = compute_overlap_time(first, second)
    expected = [("2010-01-12 12:36:00")]
    assert result == expected

def test_backwards():
    with raises(ValueError):
        time_range("2010-01-12 12:36:00", "2010-01-12 10:31:00")