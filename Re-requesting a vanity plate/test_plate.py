from plates import is_valid

def test_one():
    assert is_valid("A1234")==False
    assert is_valid("AB1234")==True

def test_two():
    assert is_valid("A")==False
    assert is_valid("")==False
    assert is_valid("AB12345")==False

def test_three():
    assert is_valid("AB12C3")==False
    assert is_valid("AB012")==False

def test_four():
    assert is_valid("AB. C,")==False


