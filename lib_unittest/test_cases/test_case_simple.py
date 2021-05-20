# Local library
from lib_unittest import mixins


class SimpleTest(mixins.TestCaseMixin):
    # Since we're using a custom mixin
    # We have a unique `self._log` available to every test case
    def test_simple_success(self):
        self._log.info('This test should pass', function='test_simple_success()')
        self.assertEqual(2, 2)

    def test_simple_error(self):
        self._log.info('This test should throw an error', function='test_simple_error()')
        self.assertEqual(2, 2/0)

    def test_simple_fail(self):
        self._log.info('This test should fail', function='test_simple_fail()')
        self.assertEqual(2, 3)
