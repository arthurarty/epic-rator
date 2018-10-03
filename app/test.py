"""
module test
"""
import unittest
from signup import Users


class TestUsers(unittest.TestCase):
    def test_signup(self):
        self.assertEqual(Users().register_user('bill','1234567','bootcamper'),\
        [{'username': 'bill', 'password': '1234567', 'role': 'bootcamper'}])

if __name__ == '__main__':
    unittest.main()