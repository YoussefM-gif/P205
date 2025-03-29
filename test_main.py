def multiply_by_6(n):
    return n * 6

def test_multiply_by_6():
    assert multiply_by_6(5) == 30
    assert multiply_by_6(0) == 0
    assert multiply_by_6(-1) == -6
