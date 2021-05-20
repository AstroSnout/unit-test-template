# Standard library
import unittest
# 3rd party library
import structlog
# Local library
from lib_unittest import ut_logging as utlog


class TestCaseMixin(unittest.TestCase):
    """
    Custom mixin for `unittest.TestCase` class in order to add unique `_log` to every test case
    """
    def __init__(self, *args, **kwargs):
        super(TestCaseMixin, self).__init__(*args, **kwargs)
        self._log: structlog.types.WrappedLogger = utlog.get_logger(self.__class__.__name__)
