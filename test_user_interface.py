import pytest
from app import welcome, signup_sign_menu

def test_welcome():
    resp = welcome()
    assert 'Welcome to Epic Rater' in resp

def test_menu():
    resp = signup_sign_menu()
    assert 'Signup' in resp