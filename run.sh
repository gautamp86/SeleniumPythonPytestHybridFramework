#!/bin/bash

# Run only sanity tests
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 -m pytest -v -s -m "sanity" --html=Reports/report.html testCases/ --browser chrome

# Run sanity OR regression tests
# pytest -v -s -m "sanity or regression" --html=Reports/report.html testCases/ --browser chrome

# Run sanity AND regression tests
# pytest -v -s -m "sanity and regression" --html=Reports/report.html testCases/ --browser chrome

# Run only regression tests
# pytest -v -s -m "regression" --html=Reports/report.html testCases/ --browser chrome

