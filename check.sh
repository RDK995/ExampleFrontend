#!/usr/bin/env sh
set -eu

grep -q "aria-label': 'Content'" index.html
grep -q "'h2'.*'Content'" index.html
grep -q "Sample content lives here" index.html
