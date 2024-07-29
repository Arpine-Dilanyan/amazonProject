import unittest
from tests_.loginTest import LoginTest


class TestSuites():
    def get_smoke_suite(self):
        pass

    def get_regression_suite(self):
        pass

    def get_performance_suite(self):
        pass

    def get_random_suite(self):
        suite = unittest.TestSuite()
        suite.addTest(LoginTest('test_positive_login'))
        return suite
