#!/bin/sh

set -eu

which virtualenv > /dev/null || (echo "Can't find virtualenv utility in PATH" && exit -1 )

virtualenv -p python3 venv

set +eu
. ./venv/bin/activate
set -eu

pip install -r requirements.txt
