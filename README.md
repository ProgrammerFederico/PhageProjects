# Phage Projects
A repository of my phage programming progression.

## Development Log
- 4.9.26 - Nucleotide Counter program initialized; designed to parse raw DNA strings and return frequency counts of each nucleotide (A, T, G, C).
- 4.10.26 - Nucleotide Counter completed;  computes count of nucleotide bases from raw DNA input.


- 4.10.26 - GC Content Calculator initialized; planned GC%, sequence length calculation features.
- 4.10.26 - GC Content Calculator completed; computes GC% from raw DNA sequences. 

- 5.25.26 - FASTA Analyzer program initialized; set up parser for .fa files and planned GC%, length, nucleotide distribution features.
- 5.29.26 - FASTA Analyzer program updated; added FASTA File input support for multi-sequence parsing.
- 6.08.26 - Nucleotide Counter along with Guanine Cytosine Calculator modularized into functions. Logic as well as efficiency improved, FASTA Analyzer parses through \n and > within FASTA files, and successful prints count of each base, as well as GC content.

- 7.10.26 - Multi Phage Analyzer program initialized; setup parser for multiple .fa files utilizing previous FASTA Analyzer.
- 8.10.26 - Multi Phage Analyzer completed; program can now discover .fa/.fasta files from a provided folder, analyze each genome using FASTA Analyzer,
and return basic statistics including total phage count, average GC content, average genome size, and GC range.