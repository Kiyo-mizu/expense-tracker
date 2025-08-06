#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Set Python path to include the current directory
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

python manage.py collectstatic --no-input
python manage.py migrate 
