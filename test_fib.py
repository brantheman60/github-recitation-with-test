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
        pytest.param(2, 1, id="2"),
        pytest.param(3, 2, id="3"),
        pytest.param(4, 3, id="4"),
        pytest.param(5, 5, id="5"),
        pytest.param(6, 8, id="6"),
        pytest.param(7, 13, id="7"),
        pytest.param(8, 21, id="8"),
        pytest.param(9, 34, id="9"),
    ]
)
def test_fib_various(n, answer):
    assert(fibonacci(n) == answer)