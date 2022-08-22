from bank import value

def test_one():
    assert value("Hello, guys")==0

def test_two():
    assert value("Hi, neighbour")==20

def test_three():
    assert value("what is up jack ?")==100