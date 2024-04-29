#!/bin/bash
set -euo pipefail # makes the script stop if any command fails

python "$1".py
pdflatex "$1".tex

rm -f ./*.aux ./*.log ./*.vscodeLog
# rm -f ./*.tex

if [[ "$OSTYPE" == "darwin"* ]]; then
    open "$1".pdf
else
    xdg-open "$1".pdf
fi
