from Calculator import *

def test_addition():
    assert add(2,3) == 5

def test_substract():
    assert sub(2,3) <= 0

def test_multiple():
    assert multi(2,3) == 6

def test_divide():
    assert div(2,3) == 0.6
