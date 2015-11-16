#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh

start_python_test 'dynamic.py'
run_python_test '2 3' "[['R0C0', 'R0C1', 'R0C2'], ['R1C0', 'R1C1', 'R1C2']]"
end_python_test
