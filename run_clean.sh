
#!bin/bash
#chmod u+x run_clean.sh



echo "Clean."

if [ "$1" == --pyc ]; then
	find . -name \*.pyc -delete
fi

find . -type d -name __pycache__ -exec rm -r {} \+

