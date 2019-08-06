
#!bin/bash
#chmod u+x run.sh


echo "Run."

python -B main.py

./run_clean.sh -pyc

find . -name \*.pyc -delete

find . -type d -name __pycache__ -exec rm -r {} \+

echo "End."