# ---- Standard library ---- #
import unittest
import shutil
# ---- Local library ------- #
from lib_unittest import globals as utg
# ---- Unit-test testcase imports ---- #
# Import testcase classes here, `unittest.main()` picks them up
from lib_unittest.test_cases.test_case_simple import SimpleTest


def _clean_up() -> None:
    utg.main_log.info('Cleaning up...')
    # Remove `./lib_unittest/dumps` folder and it's contents
    utg.main_log.info(f'Removing {utg.dumps_dir}...')
    shutil.rmtree(utg.dumps_dir)


class TestResultHandler:
    def __init__(self, test_results: unittest.result.TestResult):
        self._errors: list   = test_results.errors    # List[Tuple[unittest.case.TestCase, str]]
        self._failures: list = test_results.failures  # List[Tuple[unittest.case.TestCase, str]]

        self._total_test_count: int = test_results.testsRun
        self._test_error_count: int = len(self._errors)
        self._test_failure_count: int = len(self._failures)

    def main(self):
        if self._errors:  # Error occurred in testing
            self._on_test_error()
        elif self._failures:  # Unit test failed
            self._on_test_failure()
        else:  # All tests passed
            self._on_test_success()

    def _on_test_error(self):
        utg.main_log.error(
            'Unit testing threw errors!',
            total_test_count=self._total_test_count,
            error_test_count=self._test_error_count
        )
        return

    def _on_test_failure(self):
        # TODO - conditional cleanup - only delete dumps from tests that passed, keeping dumps of failed ones
        utg.main_log.error(
            'Unit testing failed!',
            total_test_count=self._total_test_count,
            failed_test_count=self._test_failure_count
        )
        return

    def _on_test_success(self):
        utg.main_log.info(
            'All tests finished successfully!',
            total_test_count=self._total_test_count
        )
        # Clean up if all tests passed
        _clean_up()
        return


if __name__ == '__main__':
    # ----------------- Pre-testing ------------------ #
    utg.main_log.info('Commencing Unit-testing...')
    # ----------------- Unit-testing ----------------- #
    unit_test = unittest.main(exit=False)       # unittest.main.TestProgram
    # ----------------- Post-testing ----------------- #
    TestResultHandler(unit_test.result).main()
