#!/bin/bash
# pwd is the git repo.
set -e

python manage.py test --noinput
echo 'Booyahkasha!'
