import pytest
from run import welcome

def test_welcome():
    resp = welcome()
    assert 'Welcome to Epic Rater' == resp