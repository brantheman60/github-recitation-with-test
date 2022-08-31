from fib import fibonacci
import pytest

# Test cases for the fibonacci function

def test_zeroth_fibonacci():
    assert(fibonacci(0) == 0)

def test_first_fibonacci():
    assert(fibonacci(1) == 1)

def test_21st_fibonacci():
    assert(fibonacci(21) == 10946)

def test_negative_fibonacci():
    assert(fibonacci(-1) == None)

@pytest.mark.parametrize(
    "n, answer",
    [
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
    ]
)
def test_fib_various(n, answer):
    assert(fibonacci(n) == answer)