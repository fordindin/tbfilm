import unittest
import os, sys
import logging as log
import random
from multiprocessing import Process

VERBOSITY=1
HERE = os.path.abspath(os.path.dirname(__file__))

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

def _setup_tests():
    pass

def get_suite():
    testmods = [os.path.splitext(x)[0] for x in os.listdir(HERE)
                    if x.endswith('.py') and x.startswith('test_')]
    suite = unittest.TestSuite()
    for tm in testmods:
        # ...so that the full test paths are printed on screen
        tm = "tbfilm.tests.%s" % tm
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(tm))
    return suite

def logmyname(func):
        log.debug("======= %s ======" % func.__name__)
        return(func)

def run_suite():
    _setup_tests()
    result = unittest.TextTestRunner(verbosity=VERBOSITY).run(get_suite())
    success = result.wasSuccessful()
    sys.exit(0 if success else 1)

def run_test_module_by_name(name):
    _setup_tests()
    name = os.path.splitext(os.path.basename(name))[0]
    suite = unittest.TestSuite()
    suite.addTest(unittest.defaultTestLoader.loadTestsFromName(name))
    result = unittest.TextTestRunner(verbosity=VERBOSITY).run(suite)
    success = result.wasSuccessful()
    sys.exit(0 if success else 1)


