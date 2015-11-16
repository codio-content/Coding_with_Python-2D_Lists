#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh

start_python_test 'list.py'
run_python_test '1,1,-2 -1,-2,-3 1,1,1' $'0\n-6\n3\n-3'
run_python_test '1,2,3,4 9,8,7,6 11,12' $'10\n30\n23\n63'
end_python_test
