from twttr import shorten


def test_one():
    assert shorten("ali rashwan")=="l rshwn"

def test_two():
    assert shorten("Abdallah Hamdi")=="bdllh Hmd"

def test_three():
    assert shorten("1 + 2 = 3 , 2*2=4")=="1 + 2 = 3 , 2*2=4"