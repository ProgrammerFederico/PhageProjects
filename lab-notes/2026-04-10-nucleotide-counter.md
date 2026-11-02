# Nucleotide Counter Project

**Focus:** Counting DNA bases

## Goal
Write a program to count the A, T, G, and C nucleotide bases within a DNA sequence.

## What I Did
- Wrote a Python script using `.count()`.

## What Worked
- Setting up variables, the `input()` function, and the `.count()` method.

## What Didn't Work
- Initially tried specifying a variable as `str sequence = "content"`, which isn't valid Python syntax.
- Tried using `print("A count: " + A)`, which failed because `A` was an integer and couldn't be concatenated directly with a string.

## What I Learned
- Python does not require explicit variable type declarations.
- F-strings allow strings and integers to be combined.
- Expressions and operations can also be evaluated inside f-string curly brackets `{}`.

## Automated Testing
- **Framework:** pytest
- **Test File:** `tests/test_nucleotide_counter.py`
- **Input:** `AATGCC`
- **Expected:** `{'A': 2, 'T': 1, 'C': 2, 'G': 1}`

**What Worked**
- The test passed when the expected counts matched the calculated counts.

**Key Takeaways**
- Learned about Python's assess statement, including purpose, syntax, and usage in automated testing.
- Learned that parenthesis can surround an assert statement's condition, but incorrectly placing a comma-seperated expression inside them creates a tuple. This is problematic because a nonempty tuple always evaluates to True—even when the condition inside it is false—effectively preventing the assertion from working as intended.

**Limitations**
- Only one known DNA sequence was tested.
- Empty sequences, lowercase bases, and ambiguous nucleotides remain untested.

**Next Steps**
- Expand test coverage to include boundary cases and unexpected inputs.

## Next Step
- Guanine + Cytosine Calculator!