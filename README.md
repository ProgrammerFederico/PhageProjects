# PhageProjects

**Python-based bioinformatics tools for bacteriophage genome analysis and computational biology.**

## Overview

PhageProjects documents my dynamic progression in Python programming and bioinformatics through the development of tools for analyzing bacteriophage DNA sequences.

The project began with foundational tasks such as nucleotide counting in addition to GC content calculation, and has progressively expanded into FASTA parsing, multi-genome analysis, and DNA sequence pattern detection.

Each tool is developed as an independent learning project, with accompanying laboratory-style development notes documenting implementation decisions, challenges, and lessons learned.

## Research Direction

PhageProjects serves as a computational foundation for **BHAGE (Phage Bot)**, a machine learning research project focused on predicting bacterial host associations from bacteriophage genome data.

My long-term objective is to investigate which genomic sequence characteristics are most valuable for predicting bacterial host associations in bacteriophages, and to evaluate the reliability of those predictions using experimentally documented phage–host relationships.

PhageProjects focuses on developing and validating the underlying bioinformatics tools, while BHAGE will focus on machine learning, model evaluation, and biological interpretation.

---

## Research & Development Projects

Each project explores a component of computational bacteriophage genome analysis, progressing from foundational sequence statistics to pattern detection and genomic feature extraction.

### 01. Foundational Sequence Analysis

Developed foundational tools for measuring DNA composition, calculating GC content, and processing FASTA-formatted sequences.

**Technical focus:** Sequence parsing, string processing, file handling, modular programming, and genomic statistics.

**Nucleotide Counter**

Counts individual nucleotide occurrences (A, T, C, G) within a DNA sequence.

[Source Code](projects/nucleotide_counter.py) · [Development Notes](lab-notes/2026-04-10-nucleotide-counter.md)

**GC Calculator**

Calculates the proportion of guanine and cytosine nucleotides within DNA sequences.

[Source Code](projects/gc_calculator.py) · [Development Notes](lab-notes/2026-04-10-gc-calculator.md)

**FASTA Analyzer**

Reads FASTA-formatted genome files and reports nucleotide composition, GC content, and sequence length.

[Source Code](projects/fasta_analyzer.py) · [Development Notes](lab-notes/2026-05-25-fasta-analyzer.md)

### 02. Multi-Genome Processing

Extended single-genome analysis to collections of FASTA files, enabling aggregate statistics across multiple bacteriophage genomes.

**Technical focus:** Batch processing, file discovery, dictionary-based data representation, modular program design, and statistical aggregation.

**Multi-Phage Analyzer (MPA)**

Processes multiple FASTA files from a directory and summarizes average GC content, GC range, average genome length, and total genomes analyzed.

[Source Code](projects/multi_phage_analyzer.py) · [Development Notes](lab-notes/2026-07-11-multi-phage-analyzer.md)

### 03. Sequence Pattern Analysis

Explores DNA sequence patterns and fixed-length nucleotide subsequences as a foundation for future genomic feature extraction.

**Technical focus:** Sliding-window algorithms, substring matching, motif detection, and k-mer frequency representation.

**Motif Finder**

Detects specified DNA motifs within a user-selected sequence using sliding-window matching.

[Source Code](projects/motif_finder.py) · [Development Notes](lab-notes/2026-08-11-motif-finder.md)

*Status: V1 implemented; V2 planned.*

**K-mer Frequency Analyzer**

Planned tool for extracting and counting fixed-length nucleotide subsequences within DNA sequences.

[Source Code](projects/kmer_frequency_analyzer.py)

*Status: In development; implementation pending.*

---

## Connection to BHAGE

These projects establish the computational foundations for **BHAGE (Phage Bot)**, a separate machine learning research project focused on predicting bacterial host associations from bacteriophage genomic data.

**FASTA Input → Genome Analysis → Feature Extraction → BHAGE Host Prediction**

This represents the intended research progression. The integrated machine learning pipeline remains under development.

---

## Getting Started

### Requirements

- Python 3
- A terminal or Python development environment
- DNA sequences or FASTA files, depending on the tool

The current implementations use Python's standard library.

### Running a Program

Clone the repository:

```bash
git clone https://github.com/ProgrammerFederico/PhageProjects.git
cd PhageProjects
```

For an interactive program, such as the Multi-Phage Analyzer:

```bash
python projects/multi_phage_analyzer.py
```

Follow the terminal prompt to provide a directory containing `.fa` or `.fasta` genome files.

The Nucleotide Counter, GC Calculator, and FASTA Analyzer are implemented as reusable Python functions rather than standalone interactive programs.

For detailed input requirements, usage examples, and known limitations, see the [Usage Guide](docs/usage.md).

---

## Documentation & Repository Structure

PhageProjects maintains source code alongside development notes documenting the design, implementation, challenges, and progression of each bioinformatics tool.

### Repository Structure

```text
PhageProjects/
├── projects/
│   ├── nucleotide_counter.py
│   ├── gc_calculator.py
│   ├── fasta_analyzer.py
│   ├── multi_phage_analyzer.py
│   ├── motif_finder.py
│   └── kmer_frequency_analyzer.py
│
├── lab-notes/
│   ├── index.md
│   └── [individual project notes]
│
├── tests/
├── data/
├── docs/                  
│   └── usage.md           
│
└── README.md
```

### Development Documentation

**Source Code** — Individual Python implementations of the bioinformatics tools, located in the [projects directory](projects/).

**Laboratory Notes** — Project objectives, implementation decisions, challenges, results, and next steps. See the [Lab Notes Index](lab-notes/index.md).

**Development History** — A phase-organized overview of the project's technical progression.

---

## Development History

### Phase 01 — Genome Parsing
**04–06.2026**

Developed foundational tools for nucleotide counting, GC content calculation, and FASTA genome analysis.

### Phase 02 — Multi-Genome Analysis
**07–08.2026**

Developed the Multi-Phage Analyzer to process multiple FASTA files and calculate aggregate genome statistics.

### Phase 03 — Sequence Pattern Analysis
**08–10.2026**

Implemented motif detection using sliding-window logic and initialized k-mer frequency analysis.

### Phase 04 — Feature Extraction & Validation
**Planned · 11–12.2026**

Extend motif analysis, complete k-mer extraction, and introduce automated validation.

---

## Current Development Priorities

- Extend Motif Finder to support whole-genome and region-specific searches, occurrence positions, frequency counting, and input validation.
- Complete the K-mer Frequency Analyzer.
- Introduce automated tests and improve reproducibility.
- Develop BHAGE ML V1 for bacterial host classification.

The project is actively evolving as new bioinformatics concepts and research methods are explored.