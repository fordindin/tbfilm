#!/bin/sh

: ${MODNAME:-tbfilm}

. $(dirname $0)/venv/bin/activate
python3 -m ${MODNAME} $@

