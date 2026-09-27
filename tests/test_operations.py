from src.maths_operations import add , sub

def test_add():
    assert add(2,3)==5
    assert add(5,5)==10
    assert add(9,9)==18
def test_sub():
    assert sub(11,1)==10
    assert sub(10,5)==5