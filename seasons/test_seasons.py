from seasons import Date_manipulator
import pytest


def test_seasons():
    assert Date_manipulator("2022-08-05")==1440
    assert Date_manipulator("2022-08-04")==2880


