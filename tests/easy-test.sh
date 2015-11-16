#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh

start_python_test 'easy.py'
run_python_test '"" 1,2,4 ""' '4'
run_python_test '1,2,3,4,5 9,8,7,6,5 11,22,33,44,55' '7'
end_python_test
