# Unit testing template

Barebones template for unit-testing in python with an included simple test case.

Requires `structlog` module 'cause I like it more that `logging`.

This will also create a log file `UnitTest.log` which saves stdout.

If any of the tests write to a file, it should be saved in `./lib_unittest/dumps/` folder. 
This template creates that dumps folder on execution, and deletes it when all tests have passed.
Dumps folder is not deleted if any tests fail or throw errors.