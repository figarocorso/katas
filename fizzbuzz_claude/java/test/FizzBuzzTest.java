/**
 * Simple test suite for FizzBuzz kata without external dependencies
 */
public class FizzBuzzTest {

    private static int testsPassed = 0;
    private static int testsFailed = 0;

    public static void main(String[] args) {
        System.out.println("============================================================");
        System.out.println("FizzBuzz Kata Test Suite");
        System.out.println("============================================================");

        testFizzBuzzStage1();
        testFizzBuzzStage2();

        int totalTests = testsPassed + testsFailed;
        System.out.println("\n============================================================");
        System.out.println("Results: " + testsPassed + "/" + totalTests + " tests passed");

        if (testsFailed == 0) {
            System.out.println("✓ All tests passed!");
            System.exit(0);
        } else {
            System.out.println("✗ " + testsFailed + " tests failed");
            System.exit(1);
        }
    }

    private static void testFizzBuzzStage1() {
        System.out.println("\nTesting Stage 1: Classic FizzBuzz");

        // Test numbers not divisible by 3 or 5
        assertEquals("1", FizzBuzz.fizzBuzzStage1(1), "fizzBuzzStage1(1)");
        assertEquals("2", FizzBuzz.fizzBuzzStage1(2), "fizzBuzzStage1(2)");
        assertEquals("4", FizzBuzz.fizzBuzzStage1(4), "fizzBuzzStage1(4)");
        assertEquals("7", FizzBuzz.fizzBuzzStage1(7), "fizzBuzzStage1(7)");

        // Test Fizz (divisible by 3)
        assertEquals("Fizz", FizzBuzz.fizzBuzzStage1(3), "fizzBuzzStage1(3)");
        assertEquals("Fizz", FizzBuzz.fizzBuzzStage1(6), "fizzBuzzStage1(6)");
        assertEquals("Fizz", FizzBuzz.fizzBuzzStage1(9), "fizzBuzzStage1(9)");

        // Test Buzz (divisible by 5)
        assertEquals("Buzz", FizzBuzz.fizzBuzzStage1(5), "fizzBuzzStage1(5)");
        assertEquals("Buzz", FizzBuzz.fizzBuzzStage1(10), "fizzBuzzStage1(10)");
        assertEquals("Buzz", FizzBuzz.fizzBuzzStage1(20), "fizzBuzzStage1(20)");

        // Test FizzBuzz (divisible by both)
        assertEquals("FizzBuzz", FizzBuzz.fizzBuzzStage1(15), "fizzBuzzStage1(15)");
        assertEquals("FizzBuzz", FizzBuzz.fizzBuzzStage1(30), "fizzBuzzStage1(30)");
        assertEquals("FizzBuzz", FizzBuzz.fizzBuzzStage1(45), "fizzBuzzStage1(45)");

        // Test sequence 1-20
        String[] expected = {
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
            "11", "Fizz", "13", "14", "FizzBuzz", "16", "17", "Fizz", "19", "Buzz"
        };
        boolean sequenceCorrect = true;
        for (int i = 0; i < 20; i++) {
            String result = FizzBuzz.fizzBuzzStage1(i + 1);
            if (!result.equals(expected[i])) {
                sequenceCorrect = false;
                break;
            }
        }
        if (sequenceCorrect) {
            testsPassed++;
            System.out.println("  ✓ Sequence 1-20 correct");
        } else {
            testsFailed++;
            System.out.println("  ✗ Sequence 1-20 incorrect");
        }
    }

    private static void testFizzBuzzStage2() {
        System.out.println("\nTesting Stage 2: Enhanced FizzBuzz");

        // Test numbers with no conditions
        assertEquals("1", FizzBuzz.fizzBuzzStage2(1), "fizzBuzzStage2(1)");
        assertEquals("2", FizzBuzz.fizzBuzzStage2(2), "fizzBuzzStage2(2)");
        assertEquals("4", FizzBuzz.fizzBuzzStage2(4), "fizzBuzzStage2(4)");

        // Test Fizz (divisible by 3)
        assertEquals("Fizz", FizzBuzz.fizzBuzzStage2(6), "fizzBuzzStage2(6)");
        assertEquals("Fizz", FizzBuzz.fizzBuzzStage2(9), "fizzBuzzStage2(9)");

        // Test Fizz (contains digit 3)
        assertEquals("Fizz", FizzBuzz.fizzBuzzStage2(13), "fizzBuzzStage2(13)");
        assertEquals("Fizz", FizzBuzz.fizzBuzzStage2(23), "fizzBuzzStage2(23)");
        assertEquals("Fizz", FizzBuzz.fizzBuzzStage2(31), "fizzBuzzStage2(31)");

        // Test Buzz (divisible by 5)
        assertEquals("Buzz", FizzBuzz.fizzBuzzStage2(10), "fizzBuzzStage2(10)");
        assertEquals("Buzz", FizzBuzz.fizzBuzzStage2(20), "fizzBuzzStage2(20)");

        // Test Buzz (contains digit 5) and combinations
        assertEquals("FizzBuzz", FizzBuzz.fizzBuzzStage2(51), "fizzBuzzStage2(51) - divisible by 3 + contains 5");
        assertEquals("Buzz", FizzBuzz.fizzBuzzStage2(56), "fizzBuzzStage2(56) - contains 5");

        // Test FizzBuzz (contains both 3 and 5)
        assertEquals("FizzBuzz", FizzBuzz.fizzBuzzStage2(53), "fizzBuzzStage2(53) - contains 3 and 5");

        // Test stacked results
        assertEquals("FizzBuzzBuzz", FizzBuzz.fizzBuzzStage2(35), "fizzBuzzStage2(35) - contains 3, divisible by 5, contains 5");
        assertEquals("FizzFizz", FizzBuzz.fizzBuzzStage2(3), "fizzBuzzStage2(3) - divisible by 3 AND contains 3");
        assertEquals("BuzzBuzz", FizzBuzz.fizzBuzzStage2(5), "fizzBuzzStage2(5) - divisible by 5 AND contains 5");
        assertEquals("FizzBuzzBuzz", FizzBuzz.fizzBuzzStage2(15), "fizzBuzzStage2(15) - divisible by 3, divisible by 5, contains 5");
        assertEquals("FizzFizzBuzz", FizzBuzz.fizzBuzzStage2(30), "fizzBuzzStage2(30) - divisible by 3, contains 3, divisible by 5");
    }

    private static void assertEquals(String expected, String actual, String testName) {
        if (expected.equals(actual)) {
            testsPassed++;
            System.out.println("  ✓ " + testName + " = " + actual);
        } else {
            testsFailed++;
            System.out.println("  ✗ " + testName + " = " + actual + ", expected " + expected);
        }
    }
}
