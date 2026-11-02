from projects.gc_calculator import gc_calculator


def test_gc_calculator():
    answer = gc_calculator({"A": 2, "T": 2, "C": 2, "G": 2})
    expected = 0.5

    assert answer == expected
    print(f"Test passed! Correct GC: {expected}")