from src.math_operation import add, sub

def test_add():
    assert add(2,3)==5

def test_sub():
    assert sub(5,2)==3
    assert sub(4,3)==1
    assert sub(3,3)==0
    assert sub(10,3)==7

