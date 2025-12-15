#!/usr/bin/env python3
"""Simple test runner for FizzBuzz kata without external dependencies"""

from fizzbuzz import fizzbuzz_stage1, fizzbuzz_stage2


def test_fizzbuzz_stage1():
    """Test Stage 1: Classic FizzBuzz"""
    print("Testing Stage 1: Classic FizzBuzz")
    tests_passed = 0
    tests_failed = 0

    # Test: returns number when not divisible by 3 or 5
    test_cases = [
        (1, "1"), (2, "2"), (4, "4"), (7, "7"),
        (3, "Fizz"), (6, "Fizz"), (9, "Fizz"),
        (5, "Buzz"), (10, "Buzz"), (20, "Buzz"),
        (15, "FizzBuzz"), (30, "FizzBuzz"), (45, "FizzBuzz")
    ]

    for number, expected in test_cases:
        result = fizzbuzz_stage1(number)
        if result == expected:
            tests_passed += 1
            print(f"  ✓ fizzbuzz_stage1({number}) = {result}")
        else:
            tests_failed += 1
            print(f"  ✗ fizzbuzz_stage1({number}) = {result}, expected {expected}")

    # Test sequence 1-20
    expected_sequence = [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz", "16", "17", "Fizz", "19", "Buzz"
    ]
    actual_sequence = [fizzbuzz_stage1(i) for i in range(1, 21)]

    if actual_sequence == expected_sequence:
        tests_passed += 1
        print("  ✓ Sequence 1-20 correct")
    else:
        tests_failed += 1
        print("  ✗ Sequence 1-20 incorrect")
        print(f"    Expected: {expected_sequence}")
        print(f"    Got:      {actual_sequence}")

    return tests_passed, tests_failed


def test_fizzbuzz_stage2():
    """Test Stage 2: Enhanced FizzBuzz"""
    print("\nTesting Stage 2: Enhanced FizzBuzz")
    tests_passed = 0
    tests_failed = 0

    test_cases = [
        (1, "1"), (2, "2"), (4, "4"),  # No conditions
        (6, "Fizz"), (9, "Fizz"),  # Divisible by 3
        (13, "Fizz"), (23, "Fizz"), (31, "Fizz"),  # Contains 3
        (10, "Buzz"), (20, "Buzz"),  # Divisible by 5
        (51, "FizzBuzz"), (56, "Buzz"),  # 51: divisible by 3 + contains 5; 56: contains 5
        (53, "FizzBuzz"),  # Contains both 3 and 5
        (35, "FizzBuzzBuzz"),  # Contains 3, divisible by 5, contains 5
        (3, "FizzFizz"),  # Divisible by 3 AND contains 3
        (5, "BuzzBuzz"),  # Divisible by 5 AND contains 5
        (15, "FizzBuzzBuzz"),  # Divisible by 3, divisible by 5, contains 5
        (30, "FizzFizzBuzz"),  # Divisible by 3, contains 3, divisible by 5
    ]

    for number, expected in test_cases:
        result = fizzbuzz_stage2(number)
        if result == expected:
            tests_passed += 1
            print(f"  ✓ fizzbuzz_stage2({number}) = {result}")
        else:
            tests_failed += 1
            print(f"  ✗ fizzbuzz_stage2({number}) = {result}, expected {expected}")

    return tests_passed, tests_failed


def main():
    print("=" * 60)
    print("FizzBuzz Kata Test Suite")
    print("=" * 60)

    stage1_passed, stage1_failed = test_fizzbuzz_stage1()
    stage2_passed, stage2_failed = test_fizzbuzz_stage2()

    total_passed = stage1_passed + stage2_passed
    total_failed = stage1_failed + stage2_failed
    total_tests = total_passed + total_failed

    print("\n" + "=" * 60)
    print(f"Results: {total_passed}/{total_tests} tests passed")
    if total_failed == 0:
        print("✓ All tests passed!")
        return 0
    else:
        print(f"✗ {total_failed} tests failed")
        return 1


if __name__ == "__main__":
    exit(main())
