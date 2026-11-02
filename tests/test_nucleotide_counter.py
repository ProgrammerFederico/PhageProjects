from projects.nucleotide_counter import nucleotide_counter

def test_nucleotide_counter():
    answer = nucleotide_counter("AATGCC")
    expected = {
        "A": 2,
        "T": 1,
        "C": 2,
        "G": 1
    }
    assert answer == expected
    print(f"Test passed. Correct sequence: {answer}")

    