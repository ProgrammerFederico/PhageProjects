# GC Calculator Project

**Focus:** Calculating GC content in DNA sequences

## Goal
Write a program to calculate the percentage of Guanine and Cytosine within a DNA sequence.

## What I Did
- Gathered input and assigned nucleotide counts to variables.
- Calculated the total number of bases.
- Calculated the sum of Guanine and Cytosine, then divided it by the total number of bases to determine GC content.
- Initially calculated GC percentage by multiplying the resulting fraction by 100.

## What Worked
- Finding the sum of each nucleotide base.
- Calculating GC content using the nucleotide counts.

## What Didn't Work
- Initially tried formatting GC content as `f"(((G + C) / sum * 100) + %)"`, which failed because of incorrect f-string syntax.

## What I Learned
- Proper f-string formatting, particularly the use of curly brackets `{}`.
- Using `:.2f` inside an f-string formats a numerical value to two decimal places. Example: `f"{value:.2f}"`.

## Automated Testing
- **Framework:** pytest
- **Test File:** `tests/test_gc_calculator.py`
- **Input:** `{'A': 2, 'T': 2, 'C': 2, 'G': 2}`
- **Expected:** `0.5` (50% GC content)

**What Worked**
- The test passed when the calculated GC fraction matched the expected value.
- Changing the expected value to an incorrect result triggered an `AssertionError`.
- Restoring the correct expected value allowed the test to pass again.

**Mutation Testing**
- Temporarily replaced `G + C` with `G - C` in the GC calculation.
- The mutated program returned `0.0` instead of the expected `0.5`.
- Pytest detected the incorrect calculation and failed the test with an `AssertionError`.
- Restored the original calculation and confirmed both automated tests passed.

**Key Takeaways**
- Automated tests can verify whether a program returns an expected result.
- Mutation testing evaluates whether existing tests can detect deliberately introduced defects.
- A detected mutation is referred to as a *killed mutant*.

**Limitations**
- Only one nucleotide distribution was tested.
- Empty inputs, 0% GC, 100% GC, and other boundary cases remain untested.
- Only one arithmetic mutation was evaluated.

**Next Steps**
- Expand test coverage to include boundary cases and unexpected inputs.

## Next Step
- FASTA File Analyzer