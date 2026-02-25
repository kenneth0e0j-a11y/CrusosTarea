#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python Universidad/manage.py collectstatic --no-input

python Universidad/manage.py migrate