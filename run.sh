#!/bin/bash
set -e

echo "Creating virtual environment..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Upgrading pip..."
python -m pip install --upgrade pip

echo "Installing dependencies..."
python -m pip install -r requirements.txt

echo "Running pytest..."
python -m pytest -v -s -m "sanity" --html=Reports/report.html testCases/ --browser chrome

# Run sanity OR regression tests
# pytest -v -s -m "sanity or regression" --html=Reports/report.html testCases/ --browser chrome

# Run sanity AND regression tests
# pytest -v -s -m "sanity and regression" --html=Reports/report.html testCases/ --browser chrome

# Run only regression tests
# pytest -v -s -m "regression" --html=Reports/report.html testCases/ --browser chrome

