
#!bin/bash
#chmod u+x run_unit_tests.sh



echo "Run unit tests."

python -m unittest  unit_tests.main

./run_clean.sh

echo "End."