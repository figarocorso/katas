def fizzbuzz_stage1(number: int) -> str:
    """Stage 1: Classic FizzBuzz

    Args:
        number: An integer to evaluate

    Returns:
        - "Fizz" if divisible by 3
        - "Buzz" if divisible by 5
        - "FizzBuzz" if divisible by both 3 and 5
        - The number as string otherwise
    """
    if number % 15 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)


def fizzbuzz_stage2(number: int) -> str:
    """Stage 2: Enhanced FizzBuzz with digit checking

    Args:
        number: An integer to evaluate

    Returns:
        Concatenated string of all applicable conditions:
        - "Fizz" for each: divisible by 3, contains digit 3
        - "Buzz" for each: divisible by 5, contains digit 5
        - The number as string if no conditions met
    """
    result = ""
    number_str = str(number)

    # Check for Fizz conditions
    if number % 3 == 0:
        result += "Fizz"
    if "3" in number_str:
        result += "Fizz"

    # Check for Buzz conditions
    if number % 5 == 0:
        result += "Buzz"
    if "5" in number_str:
        result += "Buzz"

    return result if result else number_str


def print_fizzbuzz_stage1(start: int = 1, end: int = 100) -> None:
    """Print FizzBuzz Stage 1 sequence"""
    for i in range(start, end + 1):
        print(fizzbuzz_stage1(i))


def print_fizzbuzz_stage2(start: int = 1, end: int = 100) -> None:
    """Print FizzBuzz Stage 2 sequence"""
    for i in range(start, end + 1):
        print(fizzbuzz_stage2(i))


if __name__ == "__main__":
    print("=== FizzBuzz Stage 1 (1-100) ===")
    print_fizzbuzz_stage1()

    print("\n=== FizzBuzz Stage 2 (1-100) ===")
    print_fizzbuzz_stage2()
