#!/usr/bin/env bash

CUR_DIR="$(pwd)"

export PYTHONPATH="${CUR_DIR}"

pushd src &> /dev/null || exit 1
if [[ "qt" == "$1" ]]; then
  pyrcc5 resources.qrc -o resources_rc.py
  python3 main.py qt
else
  python3 main.py
fi
popd &> /dev/null || exit 1

exit 0