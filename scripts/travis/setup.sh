#!/bin/bash
# pwd is the git repo.
set -e

echo "Creating test database"
psql -c 'create database plugincheck;' -U postgres
