import pytest
from fizzbuzz import fizzbuzz_stage1, fizzbuzz_stage2


class TestFizzBuzzStage1:
    """Stage 1: Classic FizzBuzz
    - Multiples of 3 -> "Fizz"
    - Multiples of 5 -> "Buzz"
    - Multiples of both -> "FizzBuzz"
    """

    def test_returns_number_when_not_divisible_by_3_or_5(self):
        assert fizzbuzz_stage1(1) == "1"
        assert fizzbuzz_stage1(2) == "2"
        assert fizzbuzz_stage1(4) == "4"
        assert fizzbuzz_stage1(7) == "7"

    def test_returns_fizz_when_divisible_by_3(self):
        assert fizzbuzz_stage1(3) == "Fizz"
        assert fizzbuzz_stage1(6) == "Fizz"
        assert fizzbuzz_stage1(9) == "Fizz"

    def test_returns_buzz_when_divisible_by_5(self):
        assert fizzbuzz_stage1(5) == "Buzz"
        assert fizzbuzz_stage1(10) == "Buzz"
        assert fizzbuzz_stage1(20) == "Buzz"

    def test_returns_fizzbuzz_when_divisible_by_both_3_and_5(self):
        assert fizzbuzz_stage1(15) == "FizzBuzz"
        assert fizzbuzz_stage1(30) == "FizzBuzz"
        assert fizzbuzz_stage1(45) == "FizzBuzz"

    def test_sequence_1_to_20(self):
        expected = [
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
            "11", "Fizz", "13", "14", "FizzBuzz", "16", "17", "Fizz", "19", "Buzz"
        ]
        result = [fizzbuzz_stage1(i) for i in range(1, 21)]
        assert result == expected


class TestFizzBuzzStage2:
    """Stage 2: Enhanced FizzBuzz
    - "Fizz" if divisible by 3 OR contains digit 3
    - "Buzz" if divisible by 5 OR contains digit 5
    - Multiple conditions can stack (e.g., 35 -> "FizzBuzzBuzz")
    """

    def test_returns_number_when_no_conditions_met(self):
        assert fizzbuzz_stage2(1) == "1"
        assert fizzbuzz_stage2(2) == "2"
        assert fizzbuzz_stage2(4) == "4"

    def test_returns_fizz_when_divisible_by_3(self):
        assert fizzbuzz_stage2(6) == "Fizz"
        assert fizzbuzz_stage2(9) == "Fizz"

    def test_returns_fizz_when_contains_digit_3(self):
        assert fizzbuzz_stage2(13) == "Fizz"
        assert fizzbuzz_stage2(23) == "Fizz"
        assert fizzbuzz_stage2(31) == "Fizz"

    def test_returns_buzz_when_divisible_by_5(self):
        assert fizzbuzz_stage2(10) == "Buzz"
        assert fizzbuzz_stage2(20) == "Buzz"

    def test_returns_buzz_when_contains_digit_5(self):
        assert fizzbuzz_stage2(51) == "Buzz"
        assert fizzbuzz_stage2(56) == "Buzz"

    def test_returns_fizzbuzz_when_contains_both_3_and_5(self):
        assert fizzbuzz_stage2(53) == "FizzBuzz"

    def test_returns_stacked_result_for_35(self):
        # 35: contains 3 (Fizz), divisible by 5 (Buzz), contains 5 (Buzz)
        assert fizzbuzz_stage2(35) == "FizzBuzzBuzz"

    def test_returns_stacked_result_for_multiple_conditions(self):
        # 3: divisible by 3 AND contains 3
        assert fizzbuzz_stage2(3) == "FizzFizz"

        # 5: divisible by 5 AND contains 5
        assert fizzbuzz_stage2(5) == "BuzzBuzz"

        # 15: divisible by 3, divisible by 5, contains 5
        assert fizzbuzz_stage2(15) == "FizzBuzzBuzz"

        # 30: divisible by 3, contains 3, divisible by 5
        assert fizzbuzz_stage2(30) == "FizzFizzBuzz"
