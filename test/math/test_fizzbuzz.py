import pytest
from algo.math import fizzbuzz

def test_fizzbuzz_with_number_5(capfd):
    fizzbuzz.solution(5)
    expected_output = """1
2
fizz
4
buzz
"""
    out, err = capfd.readouterr()
    assert out == expected_output




def test_fizzbuzz_with_number_15(capfd):
    fizzbuzz.solution(15)
    expected_output = """1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
"""
    out, err = capfd.readouterr()
    assert out == expected_output

