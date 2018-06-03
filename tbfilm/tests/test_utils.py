import unittest

from tbfilm import GetPage
from tbfilm import tests

import inspect
import logging
from tbfilm import tests

class Test_utils(tests.TestCase):

    @tests.logmyname
    def test_HTMLParser(self):
        self.assertFalse(False)

if __name__ == '__main__':
    print (__file__)
    tests.run_test_module_by_name(__file__)
