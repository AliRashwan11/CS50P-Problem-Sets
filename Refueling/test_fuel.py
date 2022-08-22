from fuel import gauge
from fuel import convert
import pytest

def test_convert():
    assert convert("1/2")==50
    assert convert("1/3")==33

   
def test_zero_div():
     with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_val_err():
     with pytest.raises(ValueError):
        convert("Cat/Dog")

def test_gauge():
    assert gauge(20)=="20%"
    assert gauge(1)=="E"
    assert gauge(99)=="F"
