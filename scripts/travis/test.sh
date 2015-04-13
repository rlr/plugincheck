#!/bin/bash
# pwd is the git repo.
set -e

export DATABASE_URL=postgres://postgres:@localhost:5432/plugincheck
python manage.py test --noinput
echo 'Booyahkasha!'
