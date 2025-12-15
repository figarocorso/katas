/**
 * FizzBuzz Kata Implementation
 * https://codingdojo.org/kata/FizzBuzz/
 */
public class FizzBuzz {

    /**
     * Stage 1: Classic FizzBuzz
     *
     * @param number An integer to evaluate
     * @return "Fizz" if divisible by 3,
     *         "Buzz" if divisible by 5,
     *         "FizzBuzz" if divisible by both 3 and 5,
     *         the number as string otherwise
     */
    public static String fizzBuzzStage1(int number) {
        if (number % 15 == 0) {
            return "FizzBuzz";
        }
        if (number % 3 == 0) {
            return "Fizz";
        }
        if (number % 5 == 0) {
            return "Buzz";
        }
        return String.valueOf(number);
    }

    /**
     * Stage 2: Enhanced FizzBuzz with digit checking
     *
     * @param number An integer to evaluate
     * @return Concatenated string of all applicable conditions:
     *         - "Fizz" for each: divisible by 3, contains digit 3
     *         - "Buzz" for each: divisible by 5, contains digit 5
     *         - The number as string if no conditions met
     */
    public static String fizzBuzzStage2(int number) {
        StringBuilder result = new StringBuilder();
        String numberStr = String.valueOf(number);

        // Check for Fizz conditions
        if (number % 3 == 0) {
            result.append("Fizz");
        }
        if (numberStr.contains("3")) {
            result.append("Fizz");
        }

        // Check for Buzz conditions
        if (number % 5 == 0) {
            result.append("Buzz");
        }
        if (numberStr.contains("5")) {
            result.append("Buzz");
        }

        return result.length() > 0 ? result.toString() : numberStr;
    }

    /**
     * Print FizzBuzz Stage 1 sequence
     */
    public static void printFizzBuzzStage1(int start, int end) {
        for (int i = start; i <= end; i++) {
            System.out.println(fizzBuzzStage1(i));
        }
    }

    /**
     * Print FizzBuzz Stage 2 sequence
     */
    public static void printFizzBuzzStage2(int start, int end) {
        for (int i = start; i <= end; i++) {
            System.out.println(fizzBuzzStage2(i));
        }
    }

    public static void main(String[] args) {
        System.out.println("=== FizzBuzz Stage 1 (1-100) ===");
        printFizzBuzzStage1(1, 100);

        System.out.println("\n=== FizzBuzz Stage 2 (1-100) ===");
        printFizzBuzzStage2(1, 100);
    }
}
