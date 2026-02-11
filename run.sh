#!/bin/bash

cd /Users/snehalpophali/Desktop/pythonautomation/SeleniumHybridFramework

# Activate virtual environment using absolute path
source /Users/snehalpophali/Desktop/pythonautomation/SeleniumHybridFramework/venv/bin/activate

# Run only sanity tests
source venv/bin/activate
python3 -m pytest -v -s -m "sanity" --html=Reports/report.html testCases/ --browser chrome

# Run sanity OR regression tests
# pytest -v -s -m "sanity or regression" --html=Reports/report.html testCases/ --browser chrome

# Run sanity AND regression tests
# pytest -v -s -m "sanity and regression" --html=Reports/report.html testCases/ --browser chrome

# Run only regression tests
# pytest -v -s -m "regression" --html=Reports/report.html testCases/ --browser chrome

