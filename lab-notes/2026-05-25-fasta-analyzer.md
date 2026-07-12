## Fasta Analyzer Project
Focus: Analyzing a FASTA File

## Goal
Write a program able to receive and process given FASTA information about a phage.

## What I Did
-  First step was figuring out how to open a python file within a nearby folder. This was done using the open() function within python.
- My second goal was to figure out how to ignore the > header within FASTA Files.
- After that was successful, I cleaned the \n from each line. 
- Finally, I took time to modularize my other 2 programs (gc_calculator.py and nucleotide_counter.py) into useable functions, which I then called.

## What Worked
- Thinking of functions as a tool that do not know each other, but can utilize each others inputs.
- Implementing a data flow with FASTA -> sequence -> counts -> GC -> output.
- Sucessfully parsed FASTA files (.fa)

## What Didn’t Work
- Assigning "textString" as a variable seemed to confuse Python. I need to read more on loops, as well as file fundamentals (opening files, extracting text, etc).
- When attempting to modularize into functions, I treated DNA as a string within the GC function. However, it was really a count dictionary, which led to confusion.
- When first attempting to call gc_calculator and nucleotide_counter, (painfully obvious now) the functions were not defined in FASTA Analyzer, so I had to import them.
- F string formatting and purpose, f strings are mainly for putting variables inside text easily.
- Recomputed counting in both functions instead of allowing them to use each other. 

## What I Learned
- While loop with open is used to read through files.
- Cleaning \n from lines.
- How to build a basic sequence-building pipeline from file input.
- Dictionaries, how to extract elements from them, and how to print elements from them.
- Defining functions, understanding their purpose, and how to use them correctly.
- Importing functions into a project.

## Next Step
- Multi-Phage Analyzation Tool.