# Python Functions Practice
# Uncomment each section and fill in the function body to complete the exercise.

# ─────────────────────────────────────────────
# 1. Basic arithmetic
# ─────────────────────────────────────────────

def add(a, b):
    """Return the sum of a and b."""
    pass  # TODO


def multiply(a, b):
    """Return the product of a and b."""
    pass  # TODO


def divide(a, b):
    """Return a divided by b. Handle division by zero by returning None."""
    pass  # TODO


# ─────────────────────────────────────────────
# 2. Strings
# ─────────────────────────────────────────────

def reverse_string(s):
    """Return s reversed."""
    pass  # TODO


def count_vowels(s):
    """Return the number of vowels (a e i o u) in s (case-insensitive)."""
    pass  # TODO


def is_palindrome(s):
    """Return True if s reads the same forwards and backwards (ignore case)."""
    pass  # TODO


# ─────────────────────────────────────────────
# 3. Lists
# ─────────────────────────────────────────────

def get_max(numbers):
    """Return the largest number in the list without using the built-in max()."""
    pass  # TODO


def flatten(nested):
    """Return a flat list from a list of lists, e.g. [[1,2],[3]] -> [1,2,3]."""
    pass  # TODO


def remove_duplicates(items):
    """Return a new list with duplicates removed, preserving order."""
    pass  # TODO


# ─────────────────────────────────────────────
# 4. Dictionaries
# ─────────────────────────────────────────────

def word_count(sentence):
    """Return a dict mapping each word to how many times it appears."""
    pass  # TODO


def invert_dict(d):
    """Return a new dict with keys and values swapped."""
    pass  # TODO


# ─────────────────────────────────────────────
# 5. Control flow
# ─────────────────────────────────────────────

def fizzbuzz(n):
    """Return a list of strings from 1 to n applying FizzBuzz rules."""
    pass  # TODO
    # Rules: multiples of 3 -> "Fizz", multiples of 5 -> "Buzz",
    #        multiples of both -> "FizzBuzz", otherwise the number as a string.


def is_prime(n):
    """Return True if n is a prime number."""
    pass  # TODO


# ─────────────────────────────────────────────
# 6. Recursion
# ─────────────────────────────────────────────

def factorial(n):
    """Return n! using recursion."""
    pass  # TODO


def fibonacci(n):
    """Return the nth Fibonacci number using recursion (0-indexed)."""
    pass  # TODO
    # fibonacci(0) == 0, fibonacci(1) == 1, fibonacci(6) == 8


# ─────────────────────────────────────────────
# Tests — run this file to check your answers
# ─────────────────────────────────────────────

def run_tests():
    results = []

    def check(name, got, expected):
        ok = got == expected
        status = "PASS" if ok else "FAIL"
        results.append(ok)
        print(f"[{status}] {name}: got {got!r}, expected {expected!r}")

    # arithmetic
    check("add(2, 3)",        add(2, 3),        5)
    check("multiply(4, 5)",   multiply(4, 5),   20)
    check("divide(10, 2)",    divide(10, 2),    5.0)
    check("divide(7, 0)",     divide(7, 0),     None)

    # strings
    check("reverse_string('hello')",  reverse_string("hello"),  "olleh")
    check("count_vowels('Python')",   count_vowels("Python"),   1)
    check("is_palindrome('racecar')", is_palindrome("racecar"), True)
    check("is_palindrome('hello')",   is_palindrome("hello"),   False)

    # lists
    check("get_max([3,1,4,1,5])",       get_max([3, 1, 4, 1, 5]),       5)
    check("flatten([[1,2],[3,4]])",      flatten([[1, 2], [3, 4]]),      [1, 2, 3, 4])
    check("remove_duplicates([1,2,1])", remove_duplicates([1, 2, 1]),   [1, 2])

    # dicts
    check("word_count('hi hi hey')", word_count("hi hi hey"), {"hi": 2, "hey": 1})
    check("invert_dict({'a':1})",    invert_dict({"a": 1}),   {1: "a"})

    # control flow
    check("fizzbuzz(15)[-1]",  fizzbuzz(15)[-1],  "FizzBuzz")
    check("is_prime(7)",       is_prime(7),        True)
    check("is_prime(9)",       is_prime(9),        False)

    # recursion
    check("factorial(5)",   factorial(5),   120)
    check("fibonacci(6)",   fibonacci(6),   8)

    passed = sum(results)
    total  = len(results)
    print(f"\n{passed}/{total} tests passed")


if __name__ == "__main__":
    run_tests()
