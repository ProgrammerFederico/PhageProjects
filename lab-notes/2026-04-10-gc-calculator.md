## GC Calculator Project
Focus: Calculating % GC in DNA Sequences

## Goal
Write a program to calculate the percentage of Guanine and Cytosine within a sequence of DNA.

## What I Did
- Gathered input, assigned counts to variables, then took the sum of each of the bases. After finding the sum of the bases, I found the sum of guanine + cytosine content. Sum of GC / sum of bases * 100 worked.

## What Worked
- Finding the sum of each of the bases.

## What Didn’t Work
- Trying to set up GC_Content as f"(((G + C) / sum *100) + %)" did not work due to improper syntax.

## What I Learned
- Proper F string formatting (most notably remembering the curly brackets).
- You can add .2f to the end of a {value} to format it as a float with 2 decimals. Example: f"{value:.2f}"

## Next Step
- FASTA File Analyzer