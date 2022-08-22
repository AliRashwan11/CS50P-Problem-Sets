from numb3rs import validate

def test_range():
    assert validate("1.1.1.1")==True
    assert validate("1.2.3.256")==False

    assert validate("1000.1000.1000.1000")==False


def test_format():
    assert validate("1.2.3")==False
    assert validate("1.2.3.4.5")==False
    assert validate("cat")==False

    