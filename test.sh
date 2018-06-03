#!/bin/sh

: ${MODNAME:=tbfilm}

. ./venv/bin/activate

set -eu

dir=$(dirname $0)/
cd $dir

SUDO=""
set +u
set -u

python3 -m ${MODNAME}.tests
