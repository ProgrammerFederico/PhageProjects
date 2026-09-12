## MOTIF Finder Project
Focus: Locate and identify patterns within genome sequences.

## Goal
Write a program able to determine motif location and frequency from a given DNA sequence/motif.

## What I Did
- Opened given file, then cleaned any iterations of "\n" and ">" (common in .FASTA/.fa files) from the raw text.
- Prompted user for sequence to search for (haystack), along with MOTIF to search for (needle).
- Used in operator to identify motifs within DNA sequences.


## What Worked
- Utilizing in operator to dig through raw text.
- Stacked if statement logic to ensure the following conditionals; 1. haystack actually exists before continuing, 2. motif exists.

## What Didn’t Work
- For loop, unneccessary because in operator already checks through every character.
- Putting the second print statement outside the if, without an else.


## What I Learned
- Refreshed on in operator.
- Else needed, as the print will run regardless if its out of the if or not (because of the first if statement).


## Additional Notes:



## Next Step
- WIP