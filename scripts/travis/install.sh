#!/bin/bash
# pwd is the git repo.
set -e

echo "Install Python dependencies"
./peep.sh install \
    -r requirements/default.txt \
    -r requirements/dev.txt

# Print the installed packages for the world to see.
pip freeze
echo
