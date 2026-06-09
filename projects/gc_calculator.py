
def gc_calculator(nucleotide_count):
    total_bases = (nucleotide_count["A"] + nucleotide_count["T"] + nucleotide_count["C"] + nucleotide_count["G"])
    gc_content = ((nucleotide_count['G'] + nucleotide_count['C']) / total_bases)
    # Formatting for later usage. printf(f"GC content: {gc_content * 100:.0f}%")
    return gc_content