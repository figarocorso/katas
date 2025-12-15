#!/bin/bash
# Script to compile and run FizzBuzz kata

BASE_DIR="/Users/miguel.julian/coding/katas/fizzbuzz_claude/java"

# Compile
echo "Compiling..."
javac "$BASE_DIR/src/FizzBuzz.java" "$BASE_DIR/test/FizzBuzzTest.java"

if [ $? -eq 0 ]; then
    echo "Compilation successful!"
    echo ""

    # Run tests
    echo "Running tests..."
    java -cp "$BASE_DIR/src:$BASE_DIR/test" FizzBuzzTest
    TEST_RESULT=$?
    echo ""

    # Run main program if tests pass
    if [ $TEST_RESULT -eq 0 ]; then
        echo "Running FizzBuzz program..."
        java -cp "$BASE_DIR/src" FizzBuzz
    fi
else
    echo "Compilation failed!"
    exit 1
fi
