from working import convert
import pytest


def test_ValueErrorRaised():
    with pytest.raises(ValueError):
        convert("13 AM to 10 PM")
    
    with pytest.raises(ValueError):
        convert("10:60 AM to 10:00 PM")

    with pytest.raises(ValueError):
        convert("10 AM until 10 PM")
    

def test_format():
    assert convert("9 AM to 10 AM")=="09:00 to 10:00"
    assert convert("9:20 AM to 10:10 PM")=="09:20 to 22:10"
    assert convert("9:50 PM to 1:00 AM")=="21:50 to 01:00"

    
