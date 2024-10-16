#!/bin/bash

cd $(dirname "$0")
echo $(pwd)
cd $(pwd)

bash -c "python3 -m pipenv run python desktop.py" &
