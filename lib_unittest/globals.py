# Standard Library
import os
# 3rd party library
import structlog
# Local library


# -------- Required paths --------
# Absolute path to './lib_unittest/'
lib_test_dir = os.path.dirname(os.path.realpath(__file__))
# Absolute path to `./unit_test.py` parent folder
# This logic assumes `lib_unittest` directory and `unit_test.py` have the same parent folder
root_dir = os.path.abspath(os.path.join(lib_test_dir, os.pardir))
# Absolute path to `./lib_unittest/samples/`
# Holds original files that unit-test results are compared to
sample_files_dir = os.path.join(lib_test_dir, 'samples')
# Absolute path to `./lib_unittest/dumps/`
# Folder where unit-tests dump their generated files, which are then compared to the ones in `./lib_unittest/samples/`
# If all tests passed, `dumps` folder and it's contents are deleted (check unit_test.py's `_clean_up()` function)
dumps_dir = os.path.join(os.path.join(lib_test_dir, 'dumps'))

# Folder creation
if not os.path.exists(dumps_dir):
    os.mkdir(os.path.join(lib_test_dir, 'dumps'))  # ./lib_unittest/dumps

# Logs
main_log: structlog.types.WrappedLogger  # Initialized in unit_test_logging.py
