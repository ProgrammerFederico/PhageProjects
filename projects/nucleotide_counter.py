
def nucleotide_counter(data):
    sequence = data
    A = sequence.count('A')
    T = sequence.count('T')
    C = sequence.count('C')
    G = sequence.count('G')
    sequenceList = {"A": A, "T": T, "C": C, "G": G}
    return sequenceList