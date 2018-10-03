import pytest
from run import *

def test_welcome():
    resp = welcome()
    assert 'Welcome to Epic Rater' in resp

def test_menu():
    resp = signup_sign_menu()
    assert 'Signup' in resp