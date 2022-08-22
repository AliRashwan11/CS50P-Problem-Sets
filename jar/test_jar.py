from jar import Jar
import pytest



def test_one():
    jar1=Jar(10)
    assert jar1.size==0
    assert jar1.capacity==10


def test_two():
    jar2=Jar(4)
    jar2.deposit(3)
    assert jar2.size==3


def test_three():
    jar3=Jar(9)
    jar3.deposit(6)
    jar3.withdraw(2)
    assert jar3.size==4


def test_four():
    jar4=Jar(21)
    with pytest.raises(Exception):
        jar4.deposit(22)
   
