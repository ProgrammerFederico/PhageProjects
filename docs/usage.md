# Usage Guide

This guide describes how to run the bioinformatics programs currently in PhageProjects. It documents **current behavior**, not planned features.

## Requirements

- Python 3
- Python standard library (no third-party packages required)
- A local copy of this repository

Clone the repository:

```bash
git clone https://github.com/ProgrammerFederico/PhageProjects.git
cd PhageProjects
```

The examples below assume you are in the repository root unless otherwise specified. Use the appropriate command for your Python installation (`python` or `python3`).

## Programs at a glance

| Program | How to use | Current status |
| --- | --- | --- |
| Nucleotide Counter | Import and call `nucleotide_counter(data)` | Implemented |
| GC Calculator | Import and call `gc_calculator(nucleotide_count)` | Implemented |
| FASTA Analyzer | Import and call `fasta_analyzer(file_path)` | Implemented |
| Multi-Phage Analyzer | Run as an interactive script | Implemented |
| Motif Finder | Run as an interactive script | Baseline version implemented |
| K-mer Frequency Analyzer | Not yet runnable | Empty placeholder; planned |

## 1. Nucleotide Counter

**Source:** [`projects/nucleotide_counter.py`](../projects/nucleotide_counter.py)

Counts uppercase `A`, `T`, `C`, and `G` characters in a supplied DNA sequence and returns a dictionary containing their respective counts.

### Usage

From the `projects` directory, in a Python interpreter:

```python
from nucleotide_counter import nucleotide_counter

nucleotide_counter("AATGC")
# {'A': 2, 'T': 1, 'C': 1, 'G': 1}
```

### Known Limitations

- The implementation is case-sensitive; lowercase nucleotides are not counted.
- Ambiguous nucleotide symbols (e.g., `N`) are ignored.
- Input validation is not implemented.

---

## 2. GC Calculator

**Source:** [`projects/gc_calculator.py`](../projects/gc_calculator.py)

Accepts a dictionary containing nucleotide counts for `A`, `T`, `C`, and `G`. Calculates and returns the GC **fraction** between 0 and 1, rather than a percentage.

### Usage

From the `projects` directory, in a Python interpreter:

```python
from gc_calculator import gc_calculator

gc_calculator({"A": 1, "T": 1, "C": 1, "G": 1})
# 0.5 (equivalent to 50%)
```

### Known Limitations

- The input dictionary must contain all four nucleotide keys.
- A total nucleotide count of zero results in a division-by-zero error.
- Input validation is not implemented.

---

## 3. FASTA Analyzer

**Source:** [`projects/fasta_analyzer.py`](../projects/fasta_analyzer.py)

Reads a FASTA file, skips lines beginning with `>`, combines remaining sequence lines, and returns a dictionary containing:

- `file_name`: input file name
- `nucleotide_count`: dictionary of A/T/C/G counts
- `gc_percentage`: GC **fraction**, despite the field name
- `genome_length`: length of the combined sequence text

From the `projects` directory, in a Python interpreter:

```python
from pathlib import Path
from fasta_analyzer import fasta_analyzer

result = fasta_analyzer(Path("../data/fastaOne.fa"))
print(result)
```

**Important:** Pass a `pathlib.Path` object, not a plain string: the function accesses `file_path.name`. Its imports also assume the `projects` directory is on Python's module search path, as in the example.

**Limitations:** Multiple FASTA records are combined into one sequence rather than analyzed separately. Lowercase bases are not counted by the nucleotide counter. Empty or invalid inputs are not handled robustly. The `gc_percentage` field stores a fraction, not a 0–100 percentage.

## 4. Multi-Phage Analyzer

**Source:** [`projects/multi_phage_analyzer.py`](../projects/multi_phage_analyzer.py)

Run from the repository root:

```bash
python projects/multi_phage_analyzer.py
```

When prompted, enter the **path to a folder** containing FASTA files, not the path to a single file. The program scans that folder for files with the exact suffixes `.fa` or `.fasta`, runs the FASTA Analyzer on each, and reports:

- Number of files analyzed (labeled as phages)
- Average GC content as a percentage
- Average genome length in base pairs
- Minimum and maximum GC percentages

If the folder contains no matching files, it prints a message and exits.

**Limitations:** Only the specified folder is scanned (not subfolders). Suffix matching is case-sensitive. An invalid folder path raises an error. An invalid or empty FASTA file may also cause an error. The reported average GC percentage is an unweighted mean of the per-file GC fractions, rather than a pooled nucleotide-weighted GC percentage.

## 5. Motif Finder (baseline)

**Source:** [`projects/motif_finder.py`](../projects/motif_finder.py)

Run from the repository root:

```bash
python projects/motif_finder.py
```

The script prompts for three inputs, in order:

1. A path to a FASTA file.
2. A DNA subsequence to locate within the file's combined sequence.
3. A motif to search for within that subsequence.

It prints whether the requested subsequence was found and, if so, whether the motif was identified within it.

**Limitations:** The current version does **not** report motif positions or occurrence counts. Matching is case-sensitive. It does not validate empty inputs or distinguish multiple FASTA records. Motif frequency and positional reporting are planned improvements, not current capabilities.

## 6. K-mer Frequency Analyzer

**Source:** [`projects/kmer_frequency_analyzer.py`](../projects/kmer_frequency_analyzer.py)

**Status:** Not implemented. The file currently contains no code. Usage instructions will be added after the implementation is complete.

## Sample data

The repository currently includes [`data/fastaOne.fa`](../data/fastaOne.fa) as a sample FASTA file. Its biological origin and reference accession are not documented here; do not assume a specific phage identity without verification.

## Research notes

See [`lab-notes/index.md`](../lab-notes/index.md) for project-by-project development records and planned next steps.

## Testing and validation

Initial automated tests are available for the Nucleotide Counter and GC Calculator in [`tests/`](../tests/). To run them, install `pytest` in your Python environment and execute `python -m pytest` from the repository root.

Testing observations and mutation-testing results are documented in the corresponding lab notes. Other programs and boundary cases have not yet been comprehensively tested; treat these tools as learning-stage implementations rather than validated research software.
