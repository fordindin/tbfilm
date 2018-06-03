import unittest
import os
import logging as log
import random
import psutil
import string
import os, time
from multiprocessing import Process

class TestCase(unittest.TestCase):

    # Print a full path representation of the single unit tests
    # being run.
    def __str__(self):
        return "%s.%s.%s" % (
            self.__class__.__module__, self.__class__.__name__,
            self._testMethodName)

    # assertRaisesRegexp renamed to assertRaisesRegex in 3.3;
    # add support for the new name.
    if not hasattr(unittest.TestCase, 'assertRaisesRegex'):
        assertRaisesRegex = unittest.TestCase.assertRaisesRegexp

# override default unittest.TestCase
unittest.TestCase = TestCase

LOGFILE="test.log"
log.basicConfig(filename=LOGFILE, level=log.DEBUG)
print("Unittest log stored at {}".format(os.path.realpath(LOGFILE)))

def run_suite():
    _setup_tests()
    result = unittest.TextTestRunner(verbosity=VERBOSITY).run(get_suite())
    success = result.wasSuccessful()
    sys.exit(0 if success else 1)

def run_test_module_by_name(name):
    # testmodules = [os.path.splitext(x)[0] for x in os.listdir(HERE)
    #                if x.endswith('.py') and x.startswith('test_')]
    _setup_tests()
    name = os.path.splitext(os.path.basename(name))[0]
    suite = unittest.TestSuite()
    suite.addTest(unittest.defaultTestLoader.loadTestsFromName(name))
    result = unittest.TextTestRunner(verbosity=VERBOSITY).run(suite)
    success = result.wasSuccessful()
    sys.exit(0 if success else 1)
